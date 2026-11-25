(function () {
  var root = document.documentElement;
  try {
    var saved = localStorage.getItem('theme');
    if (saved === 'light' || saved === 'dark') root.setAttribute('data-theme', saved);
  } catch (e) {}
  function current() {
    var t = root.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  document.addEventListener('DOMContentLoaded', function () {
    var en = root.lang === 'en';

    // Theme toggle (icon only)
    var btn = document.getElementById('theme-toggle');
    if (btn) {
      var label = function () {
        var l = current() === 'dark' ? (en ? 'Switch to light mode' : 'Passer en mode clair')
                                      : (en ? 'Switch to dark mode' : 'Passer en mode sombre');
        btn.setAttribute('aria-label', l);
        btn.title = l;
      };
      label();
      btn.addEventListener('click', function () {
        var next = current() === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        try { localStorage.setItem('theme', next); } catch (e) {}
        label();
      });
    }

    // E-mail (stocké à l'envers, révélé au clic)
    Array.prototype.forEach.call(document.querySelectorAll('.js-mail'), function (b) {
      b.addEventListener('click', function () {
        var m = b.getAttribute('data-m').split('').reverse().join('');
        var a = document.createElement('a');
        a.className = 'ext'; a.href = 'mailto:' + m; a.textContent = m;
        b.replaceWith(a); a.focus();
      });
    });

    // Mobile menu
    var menu = document.querySelector('.menu-toggle');
    var nav = document.getElementById('site-nav');
    if (menu && nav) {
      var setOpen = function (open) {
        nav.classList.toggle('open', open);
        menu.setAttribute('aria-expanded', open ? 'true' : 'false');
      };
      menu.addEventListener('click', function () { setOpen(!nav.classList.contains('open')); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
      document.addEventListener('click', function (e) {
        if (!nav.contains(e.target) && !menu.contains(e.target)) setOpen(false);
      });
      window.matchMedia('(min-width: 761px)').addEventListener('change', function () { setOpen(false); });
    }
  });
})();
