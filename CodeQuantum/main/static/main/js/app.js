$(function() {
    /* Fixed Header */
    function checkScroll(scrollOffset) {
        var header = $(".header"),
            introH = $(".intro").innerHeight();

        if (scrollOffset >= introH) {
            header.addClass("fixed");
        } else {
            header.removeClass("fixed");
        }
    }

    if ($(".header").length && $(".intro").length) {
        var scrollOffset = $(window).scrollTop();
        checkScroll(scrollOffset);

        $(window).on("scroll", function() {
            scrollOffset = $(this).scrollTop();
            checkScroll(scrollOffset);
        });
    }

    /* Smooth scroll */
    $("[data-scroll]").on("click", function(event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('scroll'),
            blockOffset = $(blockId).offset().top;

        $(".nav a").removeClass("active");
        $this.addClass("active");

        $("html, body").animate({
            scrollTop: blockOffset
        }, 500);
    });

    /* Menu nav toggle */
    $(".nav-toggle").on("click", function(event) {
        event.preventDefault();

        $(this).toggleClass("active");
        $(".nav").toggleClass("active");
    });

    /* Dropdown menu toggle */
    $(document).on('click', '.nav-item.dropdown .nav__link', function(event) {
        event.preventDefault();
        $(this).next('.dropdown-menu').toggleClass('show');
    });

    /* Slider */
    $("[data-slider]").slick({
        infinite: true,
        fade: false,
        slidesToShow: 1,
        slidesToScroll: 1
    });

    /* Validation for price input fields */
    var priceFields = ['price_in_month', 'full_price'];
    priceFields.forEach(function(fieldId) {
        var field = document.getElementById(fieldId);
        if (field) {
            field.addEventListener('input', function(event) {
                if (event.target.value < 0) {
                    event.target.value = 0;
                }
            });
        }
    });
});