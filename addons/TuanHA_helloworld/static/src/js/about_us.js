odoo.define("TuanHA_helloworld.about_us", function (require) {
  "use strict";

  async function fetchAboutUs() {
    const response = await fetch("/about_us", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    });

    if (response.ok) {
      const data = await response.json();
      document.querySelector(".about-us").innerText = data.about_us; // Đổ dữ liệu vào giao diện
    } else {
      console.error("Failed to fetch about_us");
    }
  }

  // Gọi hàm khi trang tải
  document.addEventListener("DOMContentLoaded", fetchAboutUs);
});
