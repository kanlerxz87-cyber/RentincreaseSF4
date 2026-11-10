
(function () {
  var input = document.querySelector('[data-table-search]');
  if (!input) return;
  var tables = Array.prototype.slice.call(document.querySelectorAll('main table'));
  var count = document.querySelector('[data-search-count]');
  function filter() {
    var q = input.value.trim().toLowerCase();
    var visible = 0, total = 0;
    tables.forEach(function (table) {
      Array.prototype.forEach.call(table.tBodies, function (body) {
        Array.prototype.forEach.call(body.rows, function (row) {
          total += 1;
          var show = !q || row.textContent.toLowerCase().indexOf(q) !== -1;
          row.hidden = !show;
          if (show) visible += 1;
        });
      });
    });
    if (count) count.textContent = q ? visible + ' of ' + total + ' rows match' : total + ' rows';
  }
  input.addEventListener('input', filter);
  filter();
})();
