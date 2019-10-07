$("#id-create-answer-form").on('submit', function(event){
                event.preventDefault();
                var formData = $(this).serializeArray();
                formData.push({'name': 'question', 'value': question });
                var frm = $('#id_answer_text').val('');
                $.ajax({
                    url: url_answer_question,
                    method: 'POST',
                    data: formData,
                }).done(function(data){

                    var username = data['author']['username'];
                    var pub_date = data['pub_date'];
                    var answer_text = data['answer_text'];

                    var dateTime = new Date(pub_date);
                    dateTime = moment(dateTime).format("MM-DD-YYYY HH:mm");

                    var final_html = '';
                    final_html += '<div class="box-comment">';
                    final_html += '<img class="img-circle img-sm" src="'+ static_url_image +'" alt="User Image">';
                    final_html += '<div class="comment-text"><span class="username">'+ username;
                    final_html += '<span class="text-muted pull-right">'+dateTime+'</span></span>';
                    final_html += answer_text + '</div></div>';

                    $("#box-answers").append(final_html);
                    var likes_answers = data['likes'] + ' likes - ' + data['number_answers'] + ' answers';
                    $("#question-info").html(likes_answers);

                }).fail( function( jqXHR, textStatus, errorThrown ) {
                    console.log("FAIL");
                    $('#askQuestion').modal('hide');
                    setTimeout(function(){
                        $("#error-add-alert").fadeOut();
                    }, 3000);
                });
});