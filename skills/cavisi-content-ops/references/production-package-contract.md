# Cavisi Production Package Contract

Dùng contract này khi người dùng yêu cầu content full, content hoàn chỉnh, bộ content để copy, bàn giao designer, prompt tạo ảnh, hoặc `Content Production Package`.

## 1. Định nghĩa đầu ra

`Content Production Package` là hồ sơ triển khai hoàn chỉnh cho **một content unit**. Hồ sơ phải đủ để:

- Người phụ trách copy phần công khai để đăng.
- Designer hoặc người tạo ảnh biết chính xác từng ảnh/khung cần làm gì.
- Người duyệt kiểm tra được nguồn, giới hạn, claim và trạng thái.
- Người vận hành biết lịch, CTA, KPI, repurpose và bước tiếp theo.

Không gọi một tài liệu chỉ có ý tưởng, caption ngắn hoặc danh sách prompt là `PRODUCTION-READY`.

## 2. Cấu trúc đầu ra mặc định

Khi người dùng nói rõ rằng sẽ dùng AI để tạo ảnh và muốn bản gọn, dùng **Compact AI Content Package** gồm đúng ba phần:

### A. Thông tin

- Tên bài, Content ID, ngày/giờ đăng, kênh, định dạng.
- Đối tượng, băn khoăn, mục tiêu, pillar.
- Lời hứa chính, CTA, KPI, trạng thái.
- Nguồn/review marker và dependency nếu có.

### B. Caption hoàn chỉnh

- Viết nguyên bản copy có thể đăng sau khi được duyệt.
- Với carousel hoặc Story, đặt nội dung từng ảnh/khung ngay trong caption theo nhãn `Ảnh 1`, `Ảnh 2` hoặc `Khung 1`, `Khung 2`.
- Bao gồm câu mở đầu, nội dung chính, CTA, footer Cavisi và alt text khi cần.
- Không đưa ghi chú nội bộ, prompt, nguồn chưa duyệt hoặc review marker vào phần copy công khai.

### C. Prompt thiết kế

- Một prompt tổng cho toàn bài hoặc prompt riêng theo từng ảnh/khung nếu bố cục khác nhau.
- Nêu chủ đề, số lượng ảnh, tỷ lệ, kích thước, bố cục, thứ bậc chữ, phong cách, màu sắc, icon và asset được phép dùng.
- Nêu rõ chữ tiếng Việt cần đặt trên từng ảnh nếu AI tạo ảnh có hỗ trợ chữ; nếu công cụ tạo chữ chưa ổn định, ghi phần chữ để dàn lại sau.
- Luôn có negative constraints: không mascot, không linh vật, không nhân vật đại diện, không hình trước–sau, không áo blouse/phòng lab, không badge y khoa, không fear/shame, không dùng hình ảnh như bằng chứng hiệu quả.

### D. Kiểm tra tối thiểu

- Claim, nguồn, giới hạn và wording sản phẩm đã được đánh dấu trạng thái.
- Scalp-first đã được giải thích nếu xuất hiện lần đầu.
- Tiếng Việt phù hợp người đọc 30+.
- Footer có trong bản public copy.
- Trạng thái chưa vượt quá `REVIEW` khi còn blocker.

## 3. Cấu trúc đầy đủ khi cần bàn giao sâu

Chỉ dùng cấu trúc mở rộng dưới đây khi người dùng yêu cầu brief chi tiết cho designer, nhiều phiên bản repurpose, hồ sơ duyệt sâu hoặc production handoff riêng.

### A. Metadata

- Content ID.
- Tên content.
- Ngày soạn và ngày/giờ đăng.
- Trạng thái: `IDEA`, `DRAFT`, `REVIEW`, `PRODUCTION-READY`, `PUBLISHED`, `MEASURED`.
- Phase, tuần, pillar, awareness level.
- Kênh chính, định dạng, kích thước.
- Audience, audience tension.
- Primary promise, primary CTA, KPI chính.
- Owner, approver, dependency, repurpose destination.

### B. Ý tưởng và chiến lược

- Ý tưởng lớn viết thành một câu.
- Bối cảnh hoặc quan sát đời thường.
- Tension và điều người đọc đang chưa rõ.
- Thông điệp chính.
- Content spine: hook → tension → Scalp-first reframe → role/mechanism → evidence → limitation → payoff → CTA.
- Test hypothesis nếu có.

### C. Nội dung công khai hoàn chỉnh

Với carousel, mỗi ảnh phải có riêng:

- Tên/vai trò của ảnh.
- Nội dung chính có thể copy vào thiết kế.
- Nội dung phụ hoặc dòng chuyển nếu cần.
- Vai trò của ảnh trong mạch đọc.
- Lời mời hành động nếu là ảnh CTA.

Với Story, mỗi khung phải có:

- Chữ trên khung.
- Sticker/poll/question box nếu dùng.
- Mục đích của khung.
- Điều cần ghi nhận sau khi đăng.

Ngoài phần ảnh/khung, phải có:

- Caption hoàn chỉnh.
- CTA và đường dẫn đích.
- Footer Cavisi.
- Alt text.
- Hashtag chỉ khi thật sự cần và đã được duyệt.

### D. Hướng dẫn hình ảnh và prompt

- Cảm giác hình ảnh.
- Bảng màu và kiểu chữ theo asset đã duyệt.
- Hình chụp/đồ họa/icon.
- Bố cục và khoảng an toàn.
- Prompt riêng cho từng ảnh/khung.
- Negative prompt hoặc danh sách điều cấm.
- Không mascot, linh vật hoặc nhân vật đại diện.
- Không dùng hình ảnh như bằng chứng hiệu quả.

Prompt tạo ảnh không thay thế cho brief hình ảnh. Mỗi prompt phải bám đúng nội dung và vai trò của ảnh tương ứng.

### E. Bản hướng dẫn giao việc

Phải có một đoạn handoff có thể gửi thẳng cho designer hoặc người tạo ảnh, gồm:

- Chủ đề và mục tiêu.
- Số lượng ảnh/khung.
- Phong cách.
- Nội dung bắt buộc phải đọc được.
- Asset được phép dùng.
- Hình ảnh phải tránh.
- Nguồn, giới hạn và CTA phải hiển thị thế nào.

### F. Kích thước và repurpose

- Kích thước/xuất file cho kênh chính.
- Phiên bản Story nếu có.
- Phiên bản website/FAQ nếu có.
- Phiên bản email/community nếu có.
- Alt text hoặc phần chữ có thể truy cập; không đặt thông tin quan trọng chỉ trong ảnh.

### G. Nguồn và an toàn claim

Dùng bảng:

| Nội dung | Source ID | Chủ thể | Trạng thái | Wording được phép | Giới hạn | Review |
|---|---|---|---|---|---|---|

Tách rõ brand philosophy, ingredient, formula, finished product và user outcome. Không nâng trạng thái `product-pending` thành claim thành phẩm.

### H. Đo lường và thử nghiệm

- KPI chính.
- Tín hiệu hỗ trợ.
- Hook/format/CTA đang test.
- Biến số duy nhất thay đổi trong test.
- Quy tắc đọc kết quả.
- Cách ghi nhận câu hỏi, hiểu sai và phản hồi.

### I. Checklist trước khi đăng

- Copy đã tách khỏi prompt và ghi chú nội bộ.
- Từ tiếng Anh đã dịch hoặc giải thích cho người đọc 30+.
- Scalp-first đã được giải thích ở lần đầu.
- Claim, nguồn, giới hạn, CTA và footer đã kiểm tra.
- Asset/logo/font/quyền sử dụng đã duyệt.
- Không mascot, fear, shame, pressure, trước–sau hoặc authority mượn.
- Alt text đã có.
- Người duyệt và link đích đã khóa.

## 4. Quy tắc trạng thái

- `DRAFT`: có hướng và copy sơ bộ; còn thiếu nguồn, asset hoặc wording.
- `REVIEW`: đã đủ bản thảo để duyệt; chưa được tự động đăng.
- `PRODUCTION-READY`: đủ copy, hướng ảnh, prompt, nguồn, claim map, asset, CTA, owner và approval.
- `PUBLISHED`: có link đăng thật.
- `MEASURED`: có số liệu, diễn giải có giới hạn và quyết định tối ưu.

## 5. Mức độ chi tiết mặc định

Nếu người dùng nói “viết content”, hỏi ngầm theo ngữ cảnh:

- Nếu chỉ cần định hướng: dùng `PLAN` hoặc `BRIEF`.
- Nếu cần bản gọn để AI tạo ảnh: dùng `Compact AI Content Package` với ba phần `Thông tin → Caption hoàn chỉnh → Prompt thiết kế`.
- Nếu cần bài để copy, giao designer hoặc bàn giao sâu: dùng cấu trúc đầy đủ ở mục 3.
- Nếu chưa đủ product fact/evidence: vẫn viết bản gọn hoặc đầy đủ nhưng giữ marker `[PRODUCT REVIEW]`, `[SOURCE REQUIRED]` hoặc `[PUBLICATION REVIEW]`; không lấp chỗ trống bằng suy đoán.

File mẫu `content/examples/week-01-scalp-first-carousel.md` là ví dụ tham chiếu về độ chi tiết, không phải bằng chứng để bỏ qua các review marker.
