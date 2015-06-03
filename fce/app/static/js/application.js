$(document).ready(function() {

/* Landing page behavior */

    var video_height = $('.video-wrapper').height();
    $('.video-overlay').height = video_height-100;


    $(window).resize(function() {
        video_height = $('.video-wrapper').height();
        $('.video-overlay').height() = video_height-100;
    });


    var trianglehalfwidth = $(window).innerWidth() / 2;
    $('.search-splash-triangle-down').css({
        'border-left': trianglehalfwidth+'px solid transparent',
        'border-right': trianglehalfwidth+'px solid transparent',
    });

    $(window).resize(function() {
        trianglehalfwidth = $(window).innerWidth() / 2;
        $('.search-splash-triangle-down').css({
            'border-left': trianglehalfwidth+'px solid transparent',
            'border-right': trianglehalfwidth+'px solid transparent',
        });

    });


});