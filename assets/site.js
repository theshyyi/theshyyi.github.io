(function () {
  const key = "site-language";
  const button = document.querySelector("[data-lang-toggle]");

  function setText(lang) {
    document.documentElement.lang = lang === "cn" ? "zh-CN" : "en";
    document.querySelectorAll("[data-en][data-cn]").forEach((node) => {
      node.textContent = node.dataset[lang];
    });
    document.querySelectorAll("[data-lang-panel]").forEach((node) => {
      node.hidden = node.dataset.langPanel !== lang;
    });
    if (button) {
      button.textContent = lang === "cn" ? "English" : "中文";
      button.setAttribute("aria-label", lang === "cn" ? "Switch to English" : "切换到中文");
    }
    localStorage.setItem(key, lang);
  }

  const initial = localStorage.getItem(key) || "en";
  setText(initial);

  if (button) {
    button.addEventListener("click", () => {
      const next = document.documentElement.lang === "zh-CN" ? "en" : "cn";
      setText(next);
    });
  }
})();
