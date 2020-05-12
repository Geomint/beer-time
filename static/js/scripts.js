const header = $('.main-nav');
const reviewSlideSelector = $('#review-selector')
const reviewClose = $('#review-close')

reviewSlideSelector.click(function () {
    $(".beer-page__review__form").show();
    reviewSlideSelector.hide();
    return false;
})

reviewClose.click(function () {
    $(".beer-page__review__form").hide();
    reviewSlideSelector.show();
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
    $(this.form).submit()
})

$('.checkedBox').click(function () {
    $(this.form).submit()
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