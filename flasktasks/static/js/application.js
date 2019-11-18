$("#delete-task").click(function() {
    http_delete($(this));
    return false;
});

$("#delete-mission").click(function() {
    http_delete($(this));
    return false;
});

function http_delete(element) {
    $.ajax({
        url: element.attr('href'),
        type: 'DELETE',
        success: function(result) {
            window.location.href = result;
        }
    });
}


$(document).ready(function() {
    $("p.lead").click(function() {
        //console.log('clicked');

        $('div#task_form').css("visibility", "visible");
    });
});