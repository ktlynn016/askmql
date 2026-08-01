ASKMQL.components = ASKMQL.components || {};

ASKMQL.components.bookCard = (function () {
  var icon = ASKMQL.core.icons.icon;
  var esc = ASKMQL.core.dom.escapeHtml;

  function card(book, opts) {
    opts = opts || {};
    var linkStart = opts.linkToPage ? '<a class="view-details-btn" href="book.html?id=' + book.id + '">' : '<button class="view-details-btn" onclick="ASKMQL.components.bookCard.openDetailsCallback && ASKMQL.components.bookCard.openDetailsCallback(' + book.id + ')">';
    var linkEnd = opts.linkToPage ? "</a>" : "</button>";

    return ''
      + '<div class="book-card">'
      + '  <div class="call-tab">' + esc(book.shelf.split(" ")[0]) + '</div>'
      + '  <div class="book-cover" style="background:' + book.color + '">' + icon(book.icon) + '</div>'
      + '  <div class="book-title">' + esc(book.title) + '</div>'
      + '  <div class="book-author">' + esc(book.author) + '</div>'
      + '  <div class="book-meta-row">'
      + '    <span class="badge ' + (book.available ? "available" : "unavailable") + '">' + (book.available ? "Available" : "Checked out") + '</span>'
      + '    <span class="shelf-loc">' + esc(book.shelf) + '</span>'
      + '  </div>'
      + linkStart + 'View Details' + linkEnd
      + '</div>';
  }

  function grid(books, opts) {
    return '<div class="book-grid">' + books.map(function (b) { return card(b, opts); }).join("") + '</div>';
  }

  function relatedChip(book) {
    var title = book.title.length > 28 ? book.title.slice(0, 26) + "…" : book.title;
    return ''
      + '<a class="related-chip" href="book.html?id=' + book.id + '">'
      + '  <div class="rc-cover" style="background:' + book.color + '">' + icon(book.icon) + '</div>'
      + esc(title)
      + '</a>';
  }

  return { card: card, grid: grid, relatedChip: relatedChip, openDetailsCallback: null };
})();
