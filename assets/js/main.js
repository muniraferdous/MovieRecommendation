
$(document).ready(function() {

    $("#mood").on('submit', function(event) {
        event.preventDefault();
        let emotion;
        emotion = $("input[name='emotion']:checked").val();
        console.log('You entered ' + emotion);
        $('#exampleModalCenter').modal('toggle');

        if (emotion === '') {
            alert('Empty form submitted.')
        } else {

        $.ajax( {
           type: 'POST',
           url: '',
            data: {
               name: 'emotion',
               emotion: emotion,
               csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
           },
            success:function () {
               console.log('mood submitted ;)');
            }
        });



            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("listDiv").innerHTML = this.responseText;
                }
            };
            xhttp.open("GET", 'result', true );
            xhttp.send();
        }


    });


    $("#genre").on('submit', function(event) {
        event.preventDefault();
        let genre;
        genre = $("input[name='genre']:checked").val();
        console.log('You entered ' + genre);

        $('#exampleModalCenter1').modal('toggle');


        $.ajax( {
           type: 'POST',
           url: '',
            data: {
               name: 'genre',
               emotion: genre,
               csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
           },
            success:function () {
               console.log('mood submitted ;)');
            }
        });



            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("listDiv").innerHTML = this.responseText;
                }
            };
            xhttp.open("GET", 'result', true );
            xhttp.send();



    });



    // $("#genre").on('submit',function(event) {
    //     event.preventDefault();
    //     let genres = [];
    //
    //     $.each($("input[name='genre']:checked"), function(){
    //         genres.push($(this).val());
    //     });
    //
    //     console.log(genres.length + 'selected genres: ' + genres.join(", "));
    //
    //     $('#exampleModalCenter1').modal('toggle');
    //     if (genres.length < 1) {
    //         alert('Empty form submitted.')
    //     } else {
    //         console.log(genres.length);
    //         $.ajax({
    //             type: 'POST',
    //             url: '',
    //             data: {
    //                 name: 'genre',
    //                 genre: JSON.stringify(genres),
    //                 csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
    //             },
    //             success: function () {
    //                 console.log('genres submitted ;)');
    //             }
    //         });
    //     }
    // });
});