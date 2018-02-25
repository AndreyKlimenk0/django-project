$(document).ready(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    $('.glyphicon-plus').on('click', function(e) {
        e.preventDefault();
        var urlStudentCopy = $(this).attr('href'),
            studentName = $(this).data('student-name'),
            studentSurName = $(this).data('student-surname'),
            studentTable = $(this).parents('tbody');
        $.post(urlStudentCopy, { 'csrfmiddlewaretoken': csrftoken})
        .done(function(data) {
            studentTable.append(data.stud_html)
            $('#popup').fadeIn('slow/400/fast', function() {
                $('.popup-text').text('Студет ' + studentName + ' ' + studentSurName + ' копирован')
                $(this).css({display: 'block'});
            });
            setTimeout(function() {
                $('#popup').fadeOut('slow/400/fast', function() {
                    $(this).css({diplay: 'none'})
                });
            }, 1700)
        })
        .fail(function() {
           console.log('error');
        });;
    });

    $('.glyphicon-minus').click(function(e) {
        e.preventDefault();
        var urlStudentDelete = $(this).attr('href'),
            studentName = $(this).data('student-name'),
            studentSurName = $(this).data('student-surname'),
            studentTable = $(this).parents('tr');
        $.get(urlStudentDelete)
        .done(function(data) {
            studentTable.remove()
            $('#popup').fadeIn('slow/400/fast', function() {
                $('.popup-text').text('Студет ' + studentName + ' ' + studentSurName + ' удален')
                $(this).css({display: 'block'});
            });
            setTimeout(function() {
                $('#popup').fadeOut('slow/400/fast', function() {
                    $(this).css({diplay: 'none'})
                });
            }, 1700)
        })
        .fail(function() {
            console.log('Error')
        })
    });    
});
