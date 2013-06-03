var Tags = function() {
  $('.tags_show_button').click(function() {
    var tags_show = $(".tags_show");
    if (tags_show.hasClass('moveon')) {
      $('.tags_show').removeClass('moveon').addClass('moveoff');
    } else
    {
      $('.tags_show').removeClass('moveoff').addClass('moveon');
    }
    event.preventDefault();
    $(".tags_show_button").toggleClass("active");
  });
  $('.tags_back').click(function() {
    $('.tags_show').removeClass('moveon').addClass('moveoff');
    event.preventDefault();
    $('.tags_show_button').removeClass('active');
  });
}

$(function(){
    Tags();
})