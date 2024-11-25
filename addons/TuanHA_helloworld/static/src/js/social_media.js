document.addEventListener("DOMContentLoaded", function () {
  console.log("Checking icon editable states...");

  // Lấy các phần tử input theo ID
  const twitterAccount = document.getElementById("twitter_account_0");
  const twitterIcon = document.getElementById("twitter_icon_0");

  const facebookAccount = document.getElementById("facebook_account_0");
  const facebookIcon = document.getElementById("facebook_icon_0");

  const githubAccount = document.getElementById("github_account_0");
  const githubIcon = document.getElementById("github_icon_0");

  const linkedinAccount = document.getElementById("linkedin_account_0");
  const linkedinIcon = document.getElementById("linkedin_icon_0");

  const youtubeAccount = document.getElementById("youtube_account_0");
  const youtubeIcon = document.getElementById("youtube_icon_0");

  const instagramAccount = document.getElementById("instagram_account_0");
  const instagramIcon = document.getElementById("instagram_icon_0");

  const tiktokAccount = document.getElementById("tiktok_account_0");
  const tiktokIcon = document.getElementById("tiktok_icon_0");

  const zaloAccount = document.getElementById("zalo_account_0");
  const zaloIcon = document.getElementById("zalo_icon_0");

  // Kiểm tra và xử lý từng trường tài khoản
  if (twitterAccount && twitterIcon) {
    twitterIcon.disabled = !twitterAccount.value; // Disable icon nếu không có giá trị tài khoản
  }

  if (facebookAccount && facebookIcon) {
    facebookIcon.disabled = !facebookAccount.value;
  }

  if (githubAccount && githubIcon) {
    githubIcon.disabled = !githubAccount.value;
  }

  if (linkedinAccount && linkedinIcon) {
    linkedinIcon.disabled = !linkedinAccount.value;
  }

  if (youtubeAccount && youtubeIcon) {
    youtubeIcon.disabled = !youtubeAccount.value;
  }

  if (instagramAccount && instagramIcon) {
    instagramIcon.disabled = !instagramAccount.value;
  }

  if (tiktokAccount && tiktokIcon) {
    tiktokIcon.disabled = !tiktokAccount.value;
  }

  if (zaloAccount && zaloIcon) {
    zaloIcon.disabled = !zaloAccount.value;
  }
});
