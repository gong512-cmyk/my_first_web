(function () {
  const root = document.querySelector(".home-layout");
  if (!root) return;

  const tabs = root.querySelectorAll("[data-feed-tab]");
  const cards = root.querySelectorAll("[data-feed-kind]");
  const groups = root.querySelectorAll("[data-feed-group]");

  function applyFilter(filter) {
    cards.forEach((card) => {
      const kind = card.getAttribute("data-feed-kind");
      const show = filter === "all" || kind === filter;
      card.classList.toggle("is-hidden", !show);
    });

    groups.forEach((group) => {
      const hasVisible = Array.from(group.querySelectorAll("[data-feed-kind]")).some(
        (card) => !card.classList.contains("is-hidden")
      );
      group.classList.toggle("is-hidden", !hasVisible);
    });

    tabs.forEach((tab) => {
      const active = tab.getAttribute("data-feed-tab") === filter;
      tab.classList.toggle("is-active", active);
      tab.setAttribute("aria-selected", active ? "true" : "false");
    });
  }

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => applyFilter(tab.getAttribute("data-feed-tab")));
  });

  applyFilter("all");
})();
