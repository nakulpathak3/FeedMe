$(document).ready( function() {

    $('.accordion').next('.recipe').hide();

    $('.accordion').click(function() {
        var el = $(this).parent().find('.recipe');
        if(el.hasClass("off")){
            el.slideDown();
            el.removeClass("off");
            el.addClass("on");
        }
        else if(el.hasClass("on")){
            el.slideUp();
            el.removeClass("on");
            el.addClass("off");
        }
    });
});