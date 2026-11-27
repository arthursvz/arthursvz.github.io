// Page Parcours : fiche d'une unité d'enseignement en fenêtre (popup).
// Les liens [data-ue] ouvrent la fiche ; clic/tap en dehors, bouton ou Échap la ferment.
(function () {
  var dlg = document.querySelector('.ue-dialog');
  if (!dlg || typeof dlg.showModal !== 'function') return;
  var body = dlg.querySelector('.ue-body');
  var opener = null;

  function open(id, from) {
    var tpl = document.getElementById('tpl-ue-' + id);
    if (!tpl) return false;
    body.replaceChildren(tpl.content.cloneNode(true));
    opener = from || null;
    dlg.showModal();
    document.documentElement.classList.add('ue-open');
    return true;
  }

  function close() { if (dlg.open) dlg.close(); }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest('[data-ue]');
    if (a && open(a.getAttribute('data-ue'), a)) ev.preventDefault();
  });

  // Clic/tap en dehors de la carte : la cible est la <dialog> elle-même (zone du fond).
  dlg.addEventListener('click', function (ev) { if (ev.target === dlg) close(); });
  dlg.querySelector('.ue-close').addEventListener('click', close);
  dlg.addEventListener('close', function () {
    document.documentElement.classList.remove('ue-open');
    if (opener) opener.focus({ preventScroll: true });
  });

  // Lien direct : parcours.html#ue-<id>
  var m = location.hash.match(/^#ue-(.+)$/);
  if (m) open(decodeURIComponent(m[1]));
})();
