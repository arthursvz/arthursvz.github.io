// Page Parcours : fiches en fenêtre (unités d'enseignement, certifications).
// Les liens [data-pop="<clé>"] affichent <template id="tpl-<clé>"> ;
// clic/tap en dehors, bouton ou Échap ferment la fenêtre.
(function () {
  var dlg = document.querySelector('.ue-dialog');
  if (!dlg || typeof dlg.showModal !== 'function') return;
  var body = dlg.querySelector('.ue-body');
  var opener = null;

  function open(key, from) {
    var tpl = document.getElementById('tpl-' + key);
    if (!tpl) return false;
    body.replaceChildren(tpl.content.cloneNode(true));
    if (!dlg.open) {           // une fiche peut en ouvrir une autre dans la même fenêtre
      opener = from || null;
      dlg.showModal();
    }
    document.documentElement.classList.add('ue-open');
    return true;
  }

  function close() { if (dlg.open) dlg.close(); }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('[data-pop]');
    if (a && open(a.getAttribute('data-pop'), a)) ev.preventDefault();
  });

  // Clic/tap en dehors de la carte : la cible est la <dialog> elle-même (zone du fond).
  dlg.addEventListener('click', function (ev) { if (ev.target === dlg) close(); });
  dlg.querySelector('.ue-close').addEventListener('click', close);
  dlg.addEventListener('close', function () {
    document.documentElement.classList.remove('ue-open');
    if (opener) opener.focus({ preventScroll: true });
  });

  // Lien direct : parcours.html#ue-<id> ou #cert-<id>
  if (location.hash.length > 1) open(decodeURIComponent(location.hash.slice(1)));
})();
