$(document).ready(function() {
    $('.link-modal-stud').on('click', function(event) {
        event.preventDefault();
        var hrefStudent = $(this).attr('href');
        $('#modal-student').modal('show');
        $('#modal-student div.modal-body').html('<iframe src=' + hrefStudent +
            ' width="1100" height="450" style="border:none;"></iframe>');
    });
});
    