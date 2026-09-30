$().ready(function() {
  $('.omni-onclick').each(function() {
    var pageName = $(this).text();
    $(this).click(function() {
      s.t({ pageName: pageName });
    });
  });
});
