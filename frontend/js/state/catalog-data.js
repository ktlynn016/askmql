/* Built-in dummy catalog -- mirrors backend/seeds/sample_catalog.sql
   exactly, so results match whether the app is running fully offline
   (this file) or wired to the real API. Swap ASKMQL.core.constants.USE_API
   to true to use the real backend instead. */
ASKMQL.state = ASKMQL.state || {};

ASKMQL.state.catalogData = (function () {
  var BOOKS = [
    {id:1, title:"Artificial Intelligence: A Modern Approach", author:"Stuart Russell & Peter Norvig", category:"Artificial Intelligence", year:2020, isbn:"978-0134610993",
      desc:"The standard reference on AI, covering search, knowledge representation, machine learning, and reasoning under uncertainty, with a strong emphasis on rigorous algorithmic foundations.",
      shelf:"QA76.5 R87", location:"2F · AI & Computing · Aisle 3", available:true, color:"#2563EB", icon:"brain", related:[2,6]},
    {id:2, title:"Deep Learning", author:"Ian Goodfellow, Yoshua Bengio & Aaron Courville", category:"Artificial Intelligence", year:2016, isbn:"978-0262035613",
      desc:"A comprehensive introduction to deep learning, from linear algebra foundations to convolutional and recurrent networks and modern generative models.",
      shelf:"QA76.87 G66", location:"2F · AI & Computing · Aisle 3", available:false, color:"#1D4ED8", icon:"network-wired", related:[1,6]},
    {id:3, title:"Clean Code: A Handbook of Agile Software Craftsmanship", author:"Robert C. Martin", category:"Software Engineering", year:2008, isbn:"978-0132350884",
      desc:"A practical guide to writing readable, maintainable code, with concrete rules for naming, functions, comments, and structure drawn from real refactoring examples.",
      shelf:"QA76.76 M368", location:"2F · Programming · Aisle 1", available:true, color:"#0EA5E9", icon:"broom", related:[4,5]},
    {id:4, title:"The Pragmatic Programmer", author:"David Thomas & Andrew Hunt", category:"Programming", year:2019, isbn:"978-0135957059",
      desc:"Field-tested advice on software craftsmanship, covering everything from debugging habits to automation, testing, and long-term career practices.",
      shelf:"QA76.6 T458", location:"2F · Programming · Aisle 1", available:true, color:"#3B82F6", icon:"code", related:[3,5]},
    {id:5, title:"Introduction to Algorithms", author:"Cormen, Leiserson, Rivest & Stein", category:"Programming", year:2022, isbn:"978-0262046305",
      desc:"The definitive text on algorithms and data structures, covering sorting, graph algorithms, dynamic programming, and complexity theory in depth.",
      shelf:"QA76.6 C662", location:"2F · Programming · Aisle 1", available:true, color:"#1E40AF", icon:"diagram", related:[4,3]},
    {id:6, title:"Machine Learning Yearning", author:"Andrew Ng", category:"Artificial Intelligence", year:2018, isbn:"978-1720344306",
      desc:"A practical playbook for structuring machine learning projects, diagnosing model errors, and making sound engineering decisions on real teams.",
      shelf:"Q325.5 N43", location:"2F · AI & Computing · Aisle 3", available:true, color:"#60A5FA", icon:"chart-line", related:[1,2]},
    {id:7, title:"Database System Concepts", author:"Silberschatz, Korth & Sudarshan", category:"Databases", year:2019, isbn:"978-0078022159",
      desc:"A thorough treatment of relational databases, SQL, transactions, indexing, and normalization, widely used in university database courses.",
      shelf:"QA76.9 S497", location:"1F · Databases & Networks · Aisle 5", available:true, color:"#0284C7", icon:"database", related:[8]},
    {id:8, title:"Fundamentals of Database Systems", author:"Elmasri & Navathe", category:"Databases", year:2015, isbn:"978-0133970777",
      desc:"Covers database design, ER modeling, normalization, and query optimization with an emphasis on real-world schema design.",
      shelf:"QA76.9 E46", location:"1F · Databases & Networks · Aisle 5", available:false, color:"#0369A1", icon:"server", related:[7]},
    {id:9, title:"Computer Networking: A Top-Down Approach", author:"James Kurose & Keith Ross", category:"Networking", year:2020, isbn:"978-0136681557",
      desc:"Introduces networking from the application layer down, using the internet as the primary example throughout.",
      shelf:"TK5105.5 K88", location:"1F · Databases & Networks · Aisle 6", available:true, color:"#0891B2", icon:"network-wired", related:[10]},
    {id:10, title:"CCNA 200-301 Official Cert Guide", author:"Wendell Odom", category:"Networking", year:2019, isbn:"978-0135792735",
      desc:"An exam-focused but practical guide to networking fundamentals, IP addressing, routing, and switching concepts.",
      shelf:"TK5105.5 O36", location:"1F · Databases & Networks · Aisle 6", available:true, color:"#155E75", icon:"router", related:[9]}
  ];

  var ANNOUNCEMENTS = [
    "Extended library hours this week: 7:00 AM – 8:00 PM, Monday to Friday.",
    "New arrivals in the Databases & Networks section — 12 new titles now on shelf.",
    "The library will be closed on Saturday for the annual inventory."
  ];

  function getBook(id) {
    var found = null;
    BOOKS.forEach(function (b) { if (b.id === Number(id)) found = b; });
    return found;
  }

  return { BOOKS: BOOKS, ANNOUNCEMENTS: ANNOUNCEMENTS, getBook: getBook };
})();
