$( document ).ready(function() {
        var url_data = null;
        var id = '';
        var next = null;
        var previous = null;
        var total_questions = 0;
        $("#id_closed").val('false');
        select("latest");

});

// select(option) function: Enables the option to use the same AJAX code for the questions lists.
// The input "option" corresponds to the type of list that we are going to show. Ex. "latest" or "unans"

function select(option){

        // Depending on selected option we need to load the corresponding title and variable key of the result we want to show
        if(option=="latest"){
            // When select function is invoked the list is emptied
            $("#latest").empty();
            url_data = url_data_questions;
            id=$("#latest");

        }else if(option=="unans"){

            $("#unans").empty();
            url_data = url_data_unans;
            id=$("#unans");

        }else if(option=="likes"){

            $("#likes").empty();
            url_data = url_data_likes;
            id=$("#likes");

        }

        // This AJAX call corresponds to the request of the JSON data from project API.
        $.ajax({
                url: url_data,
                method: "GET",
                dataType: 'json',
                contentType: 'application/json'
                }).done( function( data ) {

                    var dataJson=data;

                    var final_html = '';

                    var results = data['results'];

                    // Proceding to make the html for each result in the list


                    if(data['count']===0){

                        final_html += '<div class="alert alert-warning" role="alert">No Questions are available!</div></div>';

                    }else{

                        for(var i=0; i < results.length; i++){

                            var question_id = results[i]['id'];
                            var title = results[i]['title'];
                            var question_text = results[i]['question_text'];
                            var closed = results[i]['closed'];
                            var count_answers = results[i]['number_answers'];
                            var likes = results[i]['likes'];
                            var tags = results[i]['tags'];
                            var pub_date = results[i]['pub_date'];
                            var modal_class = 'apiquestion-detail" name="apiquestion-0'.replace('0', question_id);
                            var tags_html = '';


                            for(var j=0; j< tags.length; j++){
                                tags_html += '<span class="label bg-blue">'+ tags[j]['slug'] +'</span>';
                            }

                            $("#recentTags").append(tags_html);


                            final_html += '<div class="panel panel-default"><div class="panel-body"><div class="col-sm-3 text-center">';
                            final_html += '<h3>'+ count_answers +'</h3><h3> Answers</h3></div>';
                            final_html += '<div class="col-sm-3 text-center"><h3>'+ likes +'</h3><h3> Likes</h3></div><div class="col-sm-6">';

                            if( count_answers > 0){
                                final_html += '<span class="glyphicon glyphicon-fire" aria-hidden="true"></span>';
                            }

                            var dateTime = new Date(pub_date);
                            dateTime = moment(dateTime).format("MM-DD-YYYY HH:mm");

                            final_html += '<h2><a href="#detailApiQuestionModal" class="'+ modal_class +'" data-toggle="modal"';
                            final_html += ' data-target="#detailApiQuestionModal">'+ title +'</a></h2>'+ tags_html +'<h4>'+ dateTime +'</h4></div></div></div>';

                        }

                    }

                    id.html(final_html);
                    $("#total-questions").html("<h2>"+results.length+"</h2>");


                 }).fail( function( jqXHR, textStatus, errorThrown ) {
                    id.html(" ");
                 });
}

$("#id_closed").on('click', function(){

    if(this.checked){
        $(this).val("true");
    }else{
        $(this).val("false");
    }
});

$("#id-create-question-form").on('submit', function(event){
                event.preventDefault();
                var formData = $(this).serializeArray();
                $.ajax({
                    url: url_ask_question,
                    method: 'POST',
                    data: formData
                }).done(function(data){
                    $("#success-add-alert").fadeIn();
                    $('#askQuestion').modal('hide');
                    setTimeout(function(){
                        $("#success-add-alert").fadeOut();
                    }, 3000);
                }).fail( function( jqXHR, textStatus, errorThrown ) {
                    $('#askQuestion').modal('hide');
                    setTimeout(function(){
                        $("#error-add-alert").fadeOut();
                    }, 3000);
                });
});

$(document).on('click', '.apiquestion-detail', function(){
                var id = $(this).attr('name').split('-');
                id = id[1];
                var url_api = '/qapp/api/detail-question/' + id;
                var url = '/qapp/detail-question/' + id;
                var self = $(this);
                $.ajax({
                    url: url_api,
                    method: 'GET',
                    dataType: 'json',
                    contentType: 'application/json'
                }).done(function(data){

                    $("#detailApiQuestionTitle").html('Detail of  <b>' + data.title + '</b>');
                    $( "#id_detail_author" ).html(data.author.username);
                    $( "#id_detail_text" ).html(data.question_text);

                    var tags_html = '';

                    for(var j=0; j< data.tags.length; j++){
                        tags_html += '<span class="label bg-blue">'+ data.tags[j]['slug'] +'</span>';
                    }
                    $( "#id_detail_tags" ).html(tags_html);
                    $( "#id_detail_likes" ).html(data.likes);
                    console.log("Answers", $( "#see-answers" ));
                    $( "#see-answers" ).attr('href', url);
                });
                $("#detailApiQuestionModal").modal('show');
            });