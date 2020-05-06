const header = $('.main-nav');
const reviewSlideSelector = $('#review-selector')

reviewSlideSelector.click(function () {
    $(".beer-page__review__form").show();
    reviewSlideSelector.hide();
    return false;
})

$('#edit-review').click(function () {
    $(".beer-page__review__form__edit").show();
    reviewSlideSelector.hide();
    return false;
})

$(window).scroll(function () {
    if ($(window).scrollTop() > 0) {
        header.addClass('main-nav__scrolling');
    } else {
        header.removeClass('main-nav__scrolling');
    }
});

$('.favourite').click(function () {
    $('.add-to-favourites').submit();
})

$('.checkedBox').click(function () {
    $('.remove-from-favourites').submit();
})

$('.checkedBox').attr('checked', true);


$('[data-toggle="tooltip"]').tooltip();

//nav open button
$('.nav-button').on('click', function () {
    $('html').addClass('open-nav show-overlay');
});

//click to close
$('.overlay, .mobile-nav').on('click', function () {
    $('html').removeClass('open-nav show-overlay')
});