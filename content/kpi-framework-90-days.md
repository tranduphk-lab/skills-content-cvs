# Cavisi KPI Framework — 90 Ngày Đầu

**Trạng thái:** `DRAFT`  
**Giai đoạn:** 24/09/2026–22/12/2026

## Nguyên tắc đo

- 14 ngày đầu dùng để lấy baseline, không đặt target tuyệt đối khi chưa có dữ liệu lịch sử.
- Mỗi content unit có một primary KPI và tối đa ba supporting signals.
- Đo theo mục tiêu của content, không dùng view làm thước đo duy nhất.
- Phân biệt dữ liệu quan sát, diễn giải và giả thuyết nguyên nhân.
- Không suy luận causal từ một bài đăng hoặc một metric đơn lẻ.

## KPI theo tầng

| Tầng | Mục tiêu | Primary KPI | Supporting signals | Nguồn dữ liệu cần có |
|---|---|---|---|---|
| Awareness | Đúng người biết Cavisi | Qualified reach hoặc profile visits | Views, search/mention signal | Native analytics, search console |
| Attention | Người xem dừng và xem tiếp | 1–3s hold hoặc average watch time | Completion, drop-off, replay | Video analytics |
| Education | Người xem hiểu và lưu lại | Saves hoặc message recall | Source clicks, FAQ opens, comments có câu hỏi cụ thể | Social + website analytics |
| Trust | Người xem kiểm tra nguồn | Evidence/source interactions | Disclaimer opens, giảm hiểu sai trong survey | Website analytics, survey |
| Consideration | Người phù hợp tìm hiểu hệ | System/product page visits | Role exploration, qualified inquiries | Web analytics, CRM/inbox |
| Conversion | Hành động thương mại được duyệt | Approved lead/purchase event | Assisted conversion, conversion path | Ecommerce/CRM |
| Learning | Biết cơ chế nào nên lặp | Test result | Repeatability by hook/angle/format | Test log |

## Baseline capture — ngày 1–14

Ghi tối thiểu:

- Số content đã xuất bản theo pillar, angle, format, channel.
- Qualified reach, views, 1–3s hold, watch time, completion.
- Saves, shares, comments, profile visits.
- Source clicks, FAQ opens, system/product page visits.
- Câu hỏi lặp lại và objection thật.
- Tỷ lệ người mô tả đúng Cavisi và phân biệt Shampoo/Spray nếu có khảo sát.

## Review cadence

- Hàng tuần: kiểm tra attention, câu hỏi, source interaction và blocker.
- Ngày 14: khóa baseline tạm thời.
- Ngày 35: review Phase 1–2 và cập nhật topic/hook bank.
- Ngày 70: review consideration và conversion path.
- Ngày 90: tổng kết keep/revise/stop/scale và đề xuất quý sau.

## Dashboard fields

```text
content_id,date,phase,pillar,angle,awareness_level,format,channel,primary_cta,
reach,views,hold_1_3s,watch_time,completion,saves,shares,comments,
profile_visits,source_clicks,faq_opens,system_page_visits,product_page_visits,
qualified_inquiries,leads,purchases,primary_kpi,result,decision,notes
```

## Cách diễn giải

- Hold thấp: kiểm tra hook clarity, audience fit và phân phối trước khi sửa body.
- Hold tốt nhưng completion thấp: kiểm tra promise, cấu trúc và open loop.
- Completion tốt nhưng saves/source clicks thấp: kiểm tra usefulness, evidence và CTA.
- Page visits tốt nhưng inquiry thấp: kiểm tra product facts, objection và conversion path.
- Nhiều comment nhưng sai message: ưu tiên sửa clarity, không coi engagement là thành công.
