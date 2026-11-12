// Services dropdown in the header. It is a native <details>, so it already opens and closes with
// keyboard and touch; this only closes it on Escape, an outside tap, leaving it with Tab, or picking a link.
document.querySelectorAll('details.svc-menu').forEach(function (menu) {
  var summary = menu.querySelector('summary');
  document.addEventListener('click', function (e) { if (menu.open && !menu.contains(e.target)) menu.open = false; });
  menu.addEventListener('click', function (e) { if (e.target.closest('a')) menu.open = false; });
  menu.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && menu.open) { menu.open = false; summary.focus(); }
  });
  menu.addEventListener('focusout', function (e) {
    if (menu.open && e.relatedTarget && !menu.contains(e.relatedTarget)) menu.open = false;
  });
});
