/* KAIWA SUITE: shared script of index.html and get/*.html.
   No library, no call to the GitHub API. The only data it reads is the own file release/manifest.json
   (written when a release is made, see release/README.md). Without it every download shows the fallback. */
(function () {
  "use strict";
  var REPO = "https://github.com/dpkrpsk-wq/KAIWA-SUITE";
  var base = document.documentElement.getAttribute("data-base") || "";
  var MODES = {
    sw: base + "design/design-system/assets/Logos/kaiwa-icon-hell.svg",
    spectrum: base + "design/design-system/assets/Modi/kaiwa-icon-spectrum.svg",
    shift: base + "design/design-system/assets/Modi/kaiwa-icon-shift.svg"
  };

  function setMode(m) {
    if (!MODES[m]) m = "sw";
    document.documentElement.setAttribute("data-mode", m);
    var logo = document.getElementById("logo");
    if (logo) logo.src = MODES[m];
    var chips = document.querySelectorAll("[data-mode].chip");
    for (var i = 0; i < chips.length; i++) chips[i].setAttribute("aria-pressed", String(chips[i].getAttribute("data-mode") === m));
    try { localStorage.setItem("kaiwa-mode", m); } catch (e) { /* private window */ }
  }
  var saved = null;
  try { saved = localStorage.getItem("kaiwa-mode"); } catch (e) { /* no storage */ }
  setMode(saved);
  var chips = document.querySelectorAll("[data-mode].chip");
  for (var c = 0; c < chips.length; c++) chips[c].addEventListener("click", function (ev) { setMode(ev.currentTarget.getAttribute("data-mode")); });

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.textContent = text;
    return e;
  }
  function size(b) { return b >= 1048576 ? (b / 1048576).toFixed(1) + " MB" : Math.round(b / 1024) + " KB"; }
  function altSpan(parent, text) { parent.appendChild(el("span", "alt", " / " + text)); }

  var manifestPromise = fetch(base + "release/manifest.json", { cache: "no-cache" })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (m) { return m && Array.isArray(m.dateien) && m.version ? m : null; })
    .catch(function () { return null; });

  /* Each <div class="dl" data-pkg="copilot"> becomes a download button with size and SHA-256, or the fallback. */
  manifestPromise.then(function (m) {
    var boxes = document.querySelectorAll(".dl[data-pkg]");
    for (var i = 0; i < boxes.length; i++) {
      var box = boxes[i], pkg = box.getAttribute("data-pkg"), found = null;
      box.textContent = "";
      if (m) {
        var name = "KAIWA-SUITE-" + pkg + "-" + m.version + ".zip";
        for (var k = 0; k < m.dateien.length; k++) if (m.dateien[k].name === name) found = m.dateien[k];
      }
      if (found) {
        var a = el("a", "btn", "Download ZIP");
        altSpan(a, "pobierz ZIP");
        a.href = REPO + "/releases/download/v" + m.version + "/" + found.name;
        box.appendChild(a);
        box.appendChild(el("span", null, found.name + " · " + size(found.bytes) + " · " + found.dateien + " files"));
        box.appendChild(el("span", "sum", "SHA-256 " + found.sha256));
      } else {
        var p = el("p", "none", "The release is not available yet. Until then take the whole package from the main branch.");
        altSpan(p, "Wydanie nie jest jeszcze dostępne. Do tego czasu pobierz cały pakiet z gałęzi main.");
        var link = el("a", "btn plain", "Whole package (ZIP)");
        altSpan(link, "cały pakiet (ZIP)");
        link.href = REPO + "/archive/refs/heads/main.zip";
        box.appendChild(p);
        box.appendChild(link);
      }
    }
    var stamp = document.getElementById("release-stamp");
    if (stamp) stamp.textContent = m ? "release " + m.version + " · commit " + m.commit : "release not published yet";
    var whole = document.querySelectorAll("[data-whole]");
    for (var w = 0; w < whole.length; w++) whole[w].href = m ? REPO + "/archive/refs/tags/v" + m.version + ".zip" : REPO + "/archive/refs/heads/main.zip";
  });

  /* index.html: list of the files from release/sets.json, grouped by level */
  var inside = document.getElementById("inside");
  if (inside) {
    fetch(base + "release/sets.json").then(function (r) { return r.ok ? r.json() : null; }).then(function (s) {
      if (!s) return;
      var names = { copilot: "Microsoft 365 Copilot", gemini: "Google Gemini", chatgpt: "ChatGPT", claude: "Claude", any: "any / każdy" };
      var titles = { 1: ["No setup: chat and attach", "Bez konfiguracji: rozmowa w czacie"], 2: ["Configured assistant", "Stały moduł: agent, Skill, Gem, projekt"], 3: ["Files and registers", "Pliki i rejestry"], 4: ["Scripts and tests", "Skrypty i testy"] };
      for (var lv = 1; lv <= 4; lv++) {
        var h = el("div", "lv", lv + ". " + titles[lv][0]);
        altSpan(h, titles[lv][1]);
        inside.appendChild(h);
        var ul = el("ul", "items");
        s.eintraege.filter(function (e) { return e.l === lv; }).forEach(function (e) {
          var li = document.createElement("li"), a = document.createElement("a");
          a.href = REPO + (e.dir ? "/tree/main/" + e.p.replace(/\/$/, "") : "/blob/main/" + e.p);
          a.appendChild(el("b", null, names[e.v] + ": "));
          a.appendChild(document.createTextNode(e.t));
          a.appendChild(el("span", "p", e.p));
          li.appendChild(a);
          ul.appendChild(li);
        });
        inside.appendChild(ul);
      }
    }).catch(function () { /* the page works without the list */ });
  }
})();
