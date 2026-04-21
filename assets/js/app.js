(function () {
  var state = {
    lang: localStorage.getItem("site_lang") || "zh",
    posts: window.POSTS || []
  };

  function formatDate(isoDate) {
    var d = new Date(isoDate + "T00:00:00");
    if (state.lang === "zh") {
      return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
    }
    return d.toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric" });
  }

  function t(zh, en) {
    return state.lang === "zh" ? zh : en;
  }

  function getPostImages(post) {
    var list = Array.isArray(post.images) ? post.images.filter(Boolean) : [];
    if (post.image && list.indexOf(post.image) === -1) {
      list.unshift(post.image);
    }
    return list;
  }

  function setLanguage(lang) {
    state.lang = lang;
    localStorage.setItem("site_lang", lang);
    document.documentElement.setAttribute("lang", lang === "zh" ? "zh-CN" : "en");
    document.querySelectorAll("[data-i18n-zh]").forEach(function (el) {
      el.textContent = lang === "zh" ? el.getAttribute("data-i18n-zh") : el.getAttribute("data-i18n-en");
    });

    document.querySelectorAll(".lang-switch button").forEach(function (button) {
      var on = button.getAttribute("data-lang") === lang;
      button.classList.toggle("is-active", on);
      button.setAttribute("aria-pressed", on ? "true" : "false");
    });

    renderPage();
  }

  function makeCard(post) {
    var tags = post.tags.map(function (tag) {
      return '<span class="tag">#' + tag + "</span>";
    }).join("");
    var images = getPostImages(post);
    var media = images.length
      ? '<img class="post-image" src="' + images[0] + '" alt="' + (state.lang === "zh" ? post.title.zh : post.title.en) + '" loading="lazy" />'
      : "";

    return (
      '<article class="post-card ' + post.cover + '">' +
        '<a href="notes.html?post=' + post.slug + '">' +
          media +
          '<p class="post-date">' + formatDate(post.date) + "</p>" +
          '<h3>' + (state.lang === "zh" ? post.title.zh : post.title.en) + "</h3>" +
          '<p class="post-summary">' + (state.lang === "zh" ? post.summary.zh : post.summary.en) + "</p>" +
          '<div class="tag-row">' + tags + "</div>" +
        "</a>" +
      "</article>"
    );
  }

  function renderHome() {
    var holder = document.getElementById("home-posts");
    if (!holder) return;
    var latest = state.posts.slice().sort(function (a, b) {
      return a.date < b.date ? 1 : -1;
    }).slice(0, 3);
    holder.innerHTML = latest.map(makeCard).join("");
  }

  function renderTimeline() {
    var holder = document.getElementById("timeline-list");
    if (!holder) return;

    var grouped = {};
    state.posts.forEach(function (post) {
      var month = post.date.slice(0, 7);
      if (!grouped[month]) grouped[month] = [];
      grouped[month].push(post);
    });

    var keys = Object.keys(grouped).sort().reverse();
    holder.innerHTML = keys.map(function (month) {
      var items = grouped[month].sort(function (a, b) { return a.date < b.date ? 1 : -1; }).map(function (post) {
        return (
          '<li>' +
            '<a href="notes.html?post=' + post.slug + '">' +
              '<span class="timeline-date">' + formatDate(post.date) + "</span>" +
              '<span class="timeline-title">' + (state.lang === "zh" ? post.title.zh : post.title.en) + "</span>" +
            "</a>" +
          "</li>"
        );
      }).join("");

      return (
        '<section class="timeline-month">' +
          '<h3>' + month + "</h3>" +
          "<ul>" + items + "</ul>" +
        "</section>"
      );
    }).join("");
  }

  function renderNotes() {
    var list = document.getElementById("notes-list");
    var detail = document.getElementById("note-detail");
    var searchInput = document.getElementById("search-input");
    var params = new URLSearchParams(window.location.search);
    var focusSlug = params.get("post");

    if (!list || !detail) return;

    function draw(filterValue) {
      var q = (filterValue || "").trim().toLowerCase();
      var filtered = state.posts.filter(function (post) {
        var text = [post.title.zh, post.title.en, post.summary.zh, post.summary.en, post.tags.join(" ")].join(" ").toLowerCase();
        return q ? text.indexOf(q) !== -1 : true;
      }).sort(function (a, b) {
        return a.date < b.date ? 1 : -1;
      });

      list.innerHTML = filtered.map(function (post) {
        return (
          '<button class="note-item" data-slug="' + post.slug + '">' +
            '<span class="note-item-date">' + formatDate(post.date) + "</span>" +
            '<span class="note-item-title">' + (state.lang === "zh" ? post.title.zh : post.title.en) + "</span>" +
          "</button>"
        );
      }).join("");

      if (!filtered.length) {
        detail.innerHTML = '<p class="empty">' + t("没有匹配内容，换个关键词试试。", "No result. Try another keyword.") + "</p>";
        return;
      }

      var active = filtered.find(function (p) { return p.slug === focusSlug; }) || filtered[0];
      drawDetail(active);

      list.querySelectorAll(".note-item").forEach(function (button) {
        button.classList.toggle("is-active", button.getAttribute("data-slug") === active.slug);
      });
    }

    function drawDetail(post) {
      var tags = post.tags.map(function (tag) {
        return '<span class="tag">#' + tag + "</span>";
      }).join("");
      var images = getPostImages(post);
      var media = "";
      if (images.length === 1) {
        media = '<img class="note-image" src="' + images[0] + '" alt="' + (state.lang === "zh" ? post.title.zh : post.title.en) + '" loading="lazy" />';
      }
      if (images.length > 1) {
        media = '<div class="note-gallery">' + images.map(function (src, idx) {
          return '<img class="note-gallery-image" src="' + src + '" alt="' + (state.lang === "zh" ? post.title.zh : post.title.en) + ' ' + (idx + 1) + '" loading="lazy" />';
        }).join("") + '</div>';
      }

      detail.innerHTML =
        '<article class="note-article">' +
          media +
          '<p class="post-date">' + formatDate(post.date) + "</p>" +
          '<h2>' + (state.lang === "zh" ? post.title.zh : post.title.en) + "</h2>" +
          '<p class="post-summary">' + (state.lang === "zh" ? post.summary.zh : post.summary.en) + "</p>" +
          '<p class="note-content">' + (state.lang === "zh" ? post.content.zh : post.content.en) + "</p>" +
          '<div class="tag-row">' + tags + "</div>" +
        "</article>";
    }

    list.addEventListener("click", function (event) {
      var trigger = event.target.closest(".note-item");
      if (!trigger) return;
      var post = state.posts.find(function (item) { return item.slug === trigger.getAttribute("data-slug"); });
      if (!post) return;
      focusSlug = post.slug;
      draw((searchInput && searchInput.value) || "");
    });

    if (searchInput) {
      searchInput.placeholder = t("搜索标题、摘要、标签", "Search title, summary, tags");
      searchInput.addEventListener("input", function () {
        draw(searchInput.value);
      });
    }

    draw("");
  }

  function renderPage() {
    renderHome();
    renderTimeline();
    renderNotes();
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".lang-switch button").forEach(function (button) {
      button.addEventListener("click", function () {
        setLanguage(button.getAttribute("data-lang"));
      });
    });

    setLanguage(state.lang);
  });
})();
