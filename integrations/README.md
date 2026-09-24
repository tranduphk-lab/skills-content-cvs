# Notion Sync

`notion_sync.py` đồng bộ các file kế hoạch Markdown thành page con của một trang Notion. Script dùng Notion API `2026-03-11` và endpoint Markdown.

## Cấu hình

1. Tạo một internal connection trong My integrations của Notion.
2. Bật capability **Insert content** và **Update content**.
3. Kết nối connection với trang Notion cha bằng `•••` → **Connections**.
4. Từ thư mục `brand`, tạo `.env` từ `.env.example` và điền token cùng URL/page ID:

```powershell
Copy-Item .env.example .env
```

## Đồng bộ

```powershell
python integrations/notion_sync.py --all-plans
```

Mặc định đồng bộ: strategy, calendar, testing plan và KPI framework. Chọn file riêng bằng `--file`, kiểm tra bằng `--dry-run`, hoặc buộc cập nhật bằng `--force`.

Script lưu ánh xạ file → page ID tại `integrations/.notion/sync-state.json` (đã ignore). Đồng bộ một chiều: Markdown trong repo là nguồn chuẩn.

## Quy tắc format plan chi tiết

Khi file nguồn là detailed content plan, Markdown phải giữ nguyên hai lớp:

- Calendar tổng quan.
- Từng content unit theo đúng thứ tự và tên mục: Thông tin → Caption hoàn chỉnh → Prompt thiết kế.

Script đồng bộ nguyên nội dung Markdown sang Notion, không tự rút gọn, đổi tên hoặc tái cấu trúc ba mục này. Vì vậy file Markdown trong repo là nguồn chuẩn cho cả bản local và bản Notion.
