$(document).ready(function() {
    $("#mood").on('submit', function(event) {
        event.preventDefault();
        let emotion = $("input[name='emotion']:checked").val();
        console.log('You entered ' + emotion);
        $('#exampleModalCenter').modal('toggle');
        return false;
    });

    $("#genre").on('submit',function(event) {
        event.preventDefault();
        let genres = [];

        $.each($("input[name='genre']:checked"), function(){
            genres.push($(this).val());
        });

        console.log('selected genres: ' + genres.join(", "));
        $('#exampleModalCenter1').modal('toggle');
        return false;
    });
});
