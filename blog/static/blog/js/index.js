$(window).scroll(function(){
    $('nav').toggleClass('scrolled', $(this).scrollTop() > 100);
    $('#branding-logo').toggleClass('scrolled', $(this).scrollTop() > 500);
});