$(document).ready( function() {

$('.accordion').next('.recipe').hide();

$('.accordion').click(function() {
    var el = $(this).next('.recipe');
    check = (el.is(':visible')) ? el.slideUp() : ($('.recipe').slideUp()) (el.slideDown());
});

$('.stars').raty({ 
	score: 3,
	starOff: 'lib/images/star-off.png',
    starOn: 'lib/images/star-on.png'
});
});
