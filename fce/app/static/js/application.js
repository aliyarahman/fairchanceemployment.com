$(document).ready(function() {


/* Menu bar behavior */

$('#login-link, #register-link').on('click', function() {
    var panelheight = $(window).height();
    $('.login-panel').css('height', panelheight);
    $('#signin-links, #menu-button').fadeOut();
    $('.login-panel').animate({width:'toggle'},350);
    $('.login-or-register button').css('background-color', '#fff');      
    if ($(this).attr('id')=='login-link') {
       $('#login-panel-content').show();
       $('.login-or-register button').css('background-color', '#fff');      
       $('#switch-to-login button').css('background-color', '#ffdb1d');
    }
    else {
       $('#register-personal-panel-content').show();        
       $('.login-or-register button').css('background-color', '#fff');
       $('#switch-to-register button').css('background-color', '#ffdb1d');
     }
});

var menuopen = false;

$('#menu-button').on('click', function() {
    if (menuopen ===false) {
        var panelheight = $(window).height();
        $('.menu-panel').css('height', panelheight);
        $('#signin-links').fadeOut();
        $('.menu-panel').slideDown();
        menuopen = true;
    }
    else {
        $('.menu-panel').slideUp();
        $('#signin-links').fadeIn();
        menuopen = false;
    }
});



/* Login panel behavior */

$('.close-login').on('click', function() {
    $('.login-panel').animate({width:'toggle'},350);
    $('#signin-links, #menu-button').fadeIn();
    $('#register-business-panel-content, #register-personal-panel-content, #login-panel-content').hide();       
});

$('.login-or-register button').on('click', function () {
    $('.login-or-register button').css('background-color', '#fff');
    $(this).css('background-color', '#ffdb1d');
    if ($(this).parent().attr('id')=='switch-to-login') {
       $('#register-business-panel-content, #register-personal-panel-content').hide();       
       $('#login-panel-content').show();      
    }
    else {
       $('#login-panel-content').hide();        
       $('#register-personal-panel-content').show();
    }
});


$('#personal-or-business button').on('click', function () {
    if ($(this).attr('id')=='switch-to-personal') {
       $('#register-business-panel-content').hide();       
       $('#register-personal-panel-content').show();      
    }
    else {
       $('#register-personal-panel-content').hide();        
       $('#register-business-panel-content').show();
    }
});


$('.register-button').on('click', function() {
    $('.login-or-register, #login-panel-content, #register-personal-panel-content, #register-business-panel-content').hide();
    $('#registration-success').show();
});


/* Landing page behavior */

    var video_height = $('.video-wrapper').height();
    $('.video-overlay').height = video_height-100;


    $(window).resize(function() {
        video_height = $('.video-wrapper').height();
        $('.video-overlay').css('height', video_height-100);
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


/* Search page behavior */

$('.execute-search-button').on('click', function() {
    $('.search-results, .employer-profile').slideDown();
});