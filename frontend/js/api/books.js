/* Book search/detail/recommendations. Dummy mode replicates the same
   keyword logic as backend/services/retrieval/lexical.py so results
   match whichever mode is active. */
ASKMQL.api.books = (function () {
  var data = ASKMQL.state.catalogData;
  var USE_API = ASKMQL.core.constants.USE_API;

  var CATEGORY_KEYWORDS = [
    ["artificial intelligence", "Artificial Intelligence"],
    [" ai ", "Artificial Intelligence"],
    ["machine learning", "Artificial Intelligence"],
    ["program", "Programming"],
    ["database", "Databases"],
    ["network", "Networking"]
  ];

  function localSearch(text) {
    var textL = " " + text.toLowerCase() + " ";

    var titleHit = data.BOOKS.filter(function (b) {
      return b.title.toLowerCase().indexOf(text.toLowerCase()) !== -1;
    });
    if (titleHit.length) return titleHit;

    for (var i = 0; i < CATEGORY_KEYWORDS.length; i++) {
      var keyword = CATEGORY_KEYWORDS[i][0];
      var categoryName = CATEGORY_KEYWORDS[i][1];
      if (textL.indexOf(keyword) !== -1) {
        var books = data.BOOKS.filter(function (b) { return b.category === categoryName; });
        if (categoryName === "Programming") {
          books = books.concat(data.BOOKS.filter(function (b) { return b.category === "Software Engineering"; }));
        }
        if (books.length) return books;
      }
    }

    var words = textL.split(" ").filter(function (w) { return w.length > 3; });
    if (!words.length) return [];
    return data.BOOKS.filter(function (b) {
      return words.some(function (w) {
        return b.title.toLowerCase().indexOf(w) !== -1 || b.author.toLowerCase().indexOf(w) !== -1;
      });
    });
  }

  function search(text) {
    if (USE_API) return ASKMQL.api.client.get("/books?q=" + encodeURIComponent(text));
    return Promise.resolve(localSearch(text));
  }

  function getBook(id) {
    if (USE_API) return ASKMQL.api.client.get("/books/" + id);
    return Promise.resolve(data.getBook(id));
  }

  function recommend(category) {
    if (USE_API) return ASKMQL.api.client.get("/recommendations" + (category ? "?category=" + encodeURIComponent(category) : ""));
    var pool = category ? data.BOOKS.filter(function (b) { return b.category === category; }) : data.BOOKS;
    return Promise.resolve(pool.filter(function (b) { return b.available; }).slice(0, 4));
  }

  return { search: search, getBook: getBook, recommend: recommend, localSearch: localSearch };
})();
