$(document).ready( function() {

$('.accordion').next('.recipe').hide();

$('.accordion').click(function() {
    var el = $(this).next('.recipe');
    (el.hasClass('.on')) ? el.slideUp() : ($('.off').slideDown() );
});

$('#stars').raty({

});

});
