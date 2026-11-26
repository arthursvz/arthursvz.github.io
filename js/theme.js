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
  var motion = 'IntersectionObserver' in window && window.matchMedia('(prefers-reduced-motion: no-preference)').matches;
  if (motion) root.classList.add('js-reveal');
  document.addEventListener('DOMContentLoaded', function () {
    var en = root.lang === 'en';

    // Halo : parallaxe au défilement + lueur qui suit la souris
    var amb = document.querySelector('.ambient');
    if (amb && motion) {
      var layer = amb.querySelector('.layer');
      var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
      var tx = innerWidth / 2, ty = innerHeight / 3, cx = tx, cy = ty, ticking = false, moving = false;
      var onScroll = function () {
        if (ticking) return; ticking = true;
        requestAnimationFrame(function () {
          var y = Math.min(window.scrollY * 0.12, innerHeight * 0.35);
          layer.style.setProperty('--py', (-y).toFixed(1) + 'px');
          ticking = false;
        });
      };
      window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
      if (fine) {
        var step = function () {
          cx += (tx - cx) * 0.08; cy += (ty - cy) * 0.08;
          amb.style.setProperty('--mx', cx.toFixed(1) + 'px');
          amb.style.setProperty('--my', cy.toFixed(1) + 'px');
          if (Math.abs(tx - cx) + Math.abs(ty - cy) > 0.5) requestAnimationFrame(step); else moving = false;
        };
        document.addEventListener('pointermove', function (ev) {
          tx = ev.clientX; ty = ev.clientY; amb.classList.add('cursor-on');
          if (!moving) { moving = true; requestAnimationFrame(step); }
        }, { passive: true });
        document.documentElement.addEventListener('mouseleave', function () { amb.classList.remove('cursor-on'); });
      }
    }

    // Apparition douce des blocs au défilement
    if (motion) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en_) {
          if (en_.isIntersecting) { en_.target.classList.add('in'); io.unobserve(en_.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      Array.prototype.forEach.call(document.querySelectorAll('.strip, .shead, .list, .cards, .eng, .item, .cols, .rows.flush, .block > h2, .block-sm > h2, .tl li, .cgroup, .legend, .kpis, .cvprev, .ccards, .seek, .cfoot'), function (el) {
        el.classList.add('reveal'); io.observe(el);
      });
    }

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
        b.replaceWith(a);
        if (b.getAttribute('data-copy') && navigator.clipboard) {
          var c = document.createElement('button');
          c.type = 'button'; c.className = 'copy-btn'; c.textContent = b.getAttribute('data-copy');
          c.addEventListener('click', function () {
            navigator.clipboard.writeText(m).then(function () {
              c.textContent = b.getAttribute('data-copied') + ' ✓'; c.classList.add('ok');
              setTimeout(function () { c.textContent = b.getAttribute('data-copy'); c.classList.remove('ok'); }, 1800);
            });
          });
          a.after(c);
        }
        a.focus();
      });
    });

    // Heure locale (page Contact)
    Array.prototype.forEach.call(document.querySelectorAll('.js-clock'), function (el) {
      var tz = el.getAttribute('data-tz'), lg = el.getAttribute('data-lang');
      var tick = function () {
        try {
          var t = new Intl.DateTimeFormat(lg === 'en' ? 'en-GB' : 'fr-FR', { hour: '2-digit', minute: '2-digit', timeZone: tz }).format(new Date());
          el.textContent = (lg === 'en' ? ' · local time ' : ' · il y est ') + t;
          el.hidden = false;
        } catch (e) {}
      };
      tick(); setInterval(tick, 30000);
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
