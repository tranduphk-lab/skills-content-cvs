#!/usr/bin/env python3
"""Validate a machine-readable Cavisi content operations package."""
from __future__ import annotations
import json
import sys
from pathlib import Path
ALLOWED_MODES={"STRATEGY","PLAN","IDEATE","BRIEF","MEASURE","OPTIMIZE"}
ALLOWED_STATUSES={"IDEA","DRAFT","REVIEW","PRODUCTION-READY"}
REQUIRED_FIELDS={"mode","brand","status","primaryAudience","primaryPromise","primaryCta","items","sourceIds","reviewMarkers","assumptions","blockers"}
LIST_FIELDS={"items","sourceIds","reviewMarkers","assumptions","blockers"}
def validate_package(data: object) -> list[str]:
    if not isinstance(data,dict): return ["Package root must be a JSON object."]
    errors=[]
    missing=sorted(REQUIRED_FIELDS-data.keys())
    if missing: errors.append(f"Missing required fields: {', '.join(missing)}")
    if data.get("mode") not in ALLOWED_MODES: errors.append(f"Invalid mode: {data.get('mode')!r}")
    if data.get("status") not in ALLOWED_STATUSES: errors.append(f"Invalid status: {data.get('status')!r}")
    if data.get("brand") != "Cavisi": errors.append("brand must be exactly 'Cavisi'.")
    for field in LIST_FIELDS:
        if field in data and not isinstance(data[field],list): errors.append(f"{field} must be an array.")
    for field in ("primaryAudience","primaryPromise","primaryCta"):
        if not isinstance(data.get(field),str) or not data[field].strip(): errors.append(f"{field} must be a non-empty string.")
    if data.get("status")=="PRODUCTION-READY":
        if data.get("reviewMarkers"): errors.append("PRODUCTION-READY packages cannot have unresolved reviewMarkers.")
        if data.get("blockers"): errors.append("PRODUCTION-READY packages cannot have unresolved blockers.")
        if not data.get("sourceIds"): errors.append("PRODUCTION-READY packages require at least one sourceId.")
    return errors
def main()->int:
    if len(sys.argv)!=2: print("Usage: validate_content_package.py path/to/package.json"); return 2
    path=Path(sys.argv[1])
    if not path.exists(): print(f"ERROR: File not found: {path}"); return 2
    try: data=json.loads(path.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc: print(f"ERROR: Could not read valid JSON: {exc}"); return 2
    errors=validate_package(data)
    if errors:
        print("INVALID"); [print(f"- {error}") for error in errors]; return 1
    print("VALID"); return 0
if __name__=="__main__": raise SystemExit(main())
