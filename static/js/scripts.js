const header = $('.main-nav');

$(window).scroll(function () {
    if ($(window).scrollTop() > 0) {
        header.addClass('main-nav__scrolling');
    } else {
        header.removeClass('main-nav__scrolling');
    }
});

$('.favourite').click(function() {
    $('.add-to-favourites').submit();
})

$('.checkedBox').click(function() {
    $('.remove-from-favourites').submit();
})

$('.checkedBox').attr('checked', true);