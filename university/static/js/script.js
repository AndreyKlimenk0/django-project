$(document).ready(function() {
    $('.glyphicon-plus').click(function(e) {
        e.preventDefault();
        var urlStudentCopy = $(this).attr('href');
        var studentName = $(this).data('student-name');
        var studentSurName = $(this).data('student-surname');	
        $.ajax({
            async: true,
            url: urlStudentCopy,
            type: "GET",
            data: {data: 'data'},
            success: function (html) {
                $('body').html(html);
                $('#popup').fadeIn('slow/400/fast', function() {
                    $('.popup-text').text('Студет ' + studentName + ' ' + studentSurName + ' скопирован')
                    $(this).css({display: 'block'});
                setTimeout(function() {
                    $('#popup').fadeOut('slow/400/fast', function() {
                        $(this).css({data: 'none'});
                    });
                },1700);
                });
            },
        });	
    });
    $('.glyphicon-minus').click(function(e) {
        e.preventDefault();
        var urlStudentDelete = $(this).attr('href');
        var studentName = $(this).data('student-name');
        var studentSurName = $(this).data('student-surname');
        $.ajax({
            url: urlStudentDelete,
            type: "GET",
            data: {data: 'data'},
            success: function(html) {
                $('body').html(html);
                $('#popup').fadeIn('slow/400/fast', function() {
                    $('.popup-text').text('Студет ' + studentName + ' ' + studentSurName + ' удален')
                    $(this).css({display: 'block'});
                });
                setTimeout(function() {
                    $('#popup').fadeOut('slow/400/fast', function() {
                         $(this).css({display: 'none'});
                    },);
                }, 1700)
            },
        });
    });
});
