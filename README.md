<h2>Ứng dụng Web mã hóa và giải mã file sử dụng thuật toán AES</h2>

<p>Đây là một bài tập môn Nhập môn An toàn Bảo mật Thông tin, nhằm xây dựng một ứng dụng web cho phép:</p>

<ul>
  <li>Mã hóa file văn bản hoặc hình ảnh bằng thuật toán <strong>AES (Advanced Encryption Standard)</strong>.</li>
  <li>Giải mã file đã mã hóa trở về file ban đầu.</li>
  <li>Cho phép người dùng <strong>tự nhập khóa bí mật</strong>.</li>
  <li>Giao diện dễ sử dụng, thân thiện và hiện đại.</li>
  <li>Hỗ trợ tải lên và tải xuống file một cách tự động.</li>
</ul>

<h3>Giao diện chính của ứng dụng</h3>

<p align="center">
  <img src="Screenshot 2025-05-21 153411.png" alt="Giao diện AES Web App" width="600" />
</p>

<h3> Công nghệ sử dụng</h3>

<ul>
  <li><strong>Python</strong> – ngôn ngữ lập trình chính</li>
  <li><strong>Flask</strong> – framework web nhẹ</li>
  <li><strong>HTML/CSS</strong> – tạo giao diện người dùng</li>
  <li><strong>PyCryptodome</strong> – thư viện mã hóa AES</li>
</ul>

<h3>Cấu trúc thư mục</h3>

<pre>
WEB_AES/
├── app.py               # Flask backend
├── templates/           # HTML templates
├── static/              # CSS, ảnh, animation
├── uploads/             # File upload tạm thời
└── README.md            # Tài liệu mô tả bài tập
</pre>
