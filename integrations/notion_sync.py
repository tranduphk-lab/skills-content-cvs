#!/usr/bin/env python3
"""Sync Cavisi Markdown plans to Notion child pages."""
from __future__ import annotations
import argparse, hashlib, json, os, re, sys, urllib.error, urllib.request
from pathlib import Path
from typing import Any
BASE="https://api.notion.com/v1"; VERSION="2026-03-11"; BRAND=Path(__file__).resolve().parents[1]
STATE=BRAND/"integrations"/".notion"/"sync-state.json"
DEFAULTS=[BRAND/"content"/x for x in ("content-strategy-90-days.md","content-calendar-90-days.md","testing-plan-90-days.md","kpi-framework-90-days.md")]
class NotionError(RuntimeError): pass
def dotenv(path):
    if not path.exists(): return
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        line=raw.strip()
        if line and not line.startswith("#") and "=" in line:
            key,value=line.split("=",1); os.environ.setdefault(key.strip(),value.strip().strip('"').strip("'"))
def request(method, endpoint, token, payload: dict[str,Any]|None=None):
    data=json.dumps(payload,ensure_ascii=False).encode() if payload is not None else None
    req=urllib.request.Request(BASE+endpoint,data=data,method=method,headers={"Authorization":f"Bearer {token}","Notion-Version":VERSION,"Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(req,timeout=60) as response: return json.loads(response.read().decode())
    except urllib.error.HTTPError as error:
        text=error.read().decode(errors="replace")
        try: detail=json.loads(text).get("message",text)
        except json.JSONDecodeError: detail=text
        raise NotionError(f"Notion API {error.code}: {detail}") from error
    except urllib.error.URLError as error: raise NotionError(f"Không thể kết nối Notion API: {error.reason}") from error
def page_id(value):
    compact=value.replace("-",""); match=re.search(r"([0-9a-fA-F]{32})(?:[?#]|$)",compact)
    if not match: raise ValueError("NOTION_PARENT_PAGE_ID phải là page ID hoặc URL Notion hợp lệ.")
    raw=match.group(1).lower(); return "-".join((raw[:8],raw[8:12],raw[12:16],raw[16:20],raw[20:]))
def title(markdown,fallback):
    match=re.search(r"^#\s+(.+?)\s*$",markdown,re.M); value=match.group(1) if match else fallback.replace("-"," ").title()
    return re.sub(r"[*_`]","",value).strip()[:200]
def props(value): return {"title":{"type":"title","title":[{"type":"text","text":{"content":value}}]}}
def load_state(path):
    if not path.exists(): return {"version":1,"pages":{}}
    data=json.loads(path.read_text(encoding="utf-8")); data.setdefault("pages",{}); return data
def save_state(path,data):
    path.parent.mkdir(parents=True,exist_ok=True); temp=path.with_suffix(".tmp")
    temp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); temp.replace(path)
def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    dotenv(BRAND/".env"); dotenv(Path.cwd()/".env")
    parser=argparse.ArgumentParser(description="Đồng bộ kế hoạch Cavisi sang Notion")
    parser.add_argument("--file",action="append",dest="files"); parser.add_argument("--all-plans",action="store_true"); parser.add_argument("--force",action="store_true"); parser.add_argument("--dry-run",action="store_true")
    args=parser.parse_args(); files=DEFAULTS if args.all_plans or not args.files else [Path(x).expanduser().resolve() for x in args.files]
    missing=[str(x) for x in files if not x.is_file()]
    if missing: raise FileNotFoundError("Không tìm thấy file: "+", ".join(missing))
    token=os.getenv("NOTION_TOKEN","").strip(); parent=os.getenv("NOTION_PARENT_PAGE_ID","").strip()
    if not args.dry_run and (not token or not parent): raise ValueError("Cần đặt NOTION_TOKEN và NOTION_PARENT_PAGE_ID trong brand/.env.")
    parent=page_id(parent) if parent else "dry-run"; data=load_state(STATE); counts={"created":0,"updated":0,"skipped":0,"dry-run":0}
    for path in files:
        source=path.read_text(encoding="utf-8-sig"); resolved=path.resolve()
        name=resolved.relative_to(BRAND).as_posix() if resolved.is_relative_to(BRAND) else str(resolved); page_title=title(source,path.stem)
        content=re.sub(r"\A(?:\ufeff)?#\s+[^\n]+\n+","",source,count=1).lstrip(); digest=hashlib.sha256((page_title+"\n"+content).encode()).hexdigest(); previous=data["pages"].get(name,{})
        if previous.get("sha256")==digest and not args.force: print(f"Bỏ qua (không đổi): {name}"); counts["skipped"]+=1; continue
        if args.dry_run: print(f"[dry-run] {'Cập nhật' if previous.get('page_id') else 'Tạo mới'}: {name}"); counts["dry-run"]+=1; continue
        if previous.get("page_id"):
            request("PATCH",f"/pages/{previous['page_id']}",token,{"properties":props(page_title)}); request("PATCH",f"/pages/{previous['page_id']}/markdown",token,{"type":"replace_content","replace_content":{"new_str":content}}); page=previous; action="updated"
        else:
            page=request("POST","/pages",token,{"parent":{"type":"page_id","page_id":parent},"properties":props(page_title),"markdown":content}); action="created"
        data["pages"][name]={"page_id":page["id"],"url":page.get("url",previous.get("url")),"title":page_title,"sha256":digest}; save_state(STATE,data); counts[action]+=1; print(f"{action}: {name}")
    print(f"Hoàn tất: {counts['created']} tạo mới, {counts['updated']} cập nhật, {counts['skipped']} bỏ qua, {counts['dry-run']} mô phỏng.")
if __name__=="__main__":
    try: main()
    except (FileNotFoundError,ValueError,NotionError,json.JSONDecodeError) as error: print(f"Lỗi: {error}",file=sys.stderr); raise SystemExit(1)

