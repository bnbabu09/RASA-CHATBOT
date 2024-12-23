function send() {
  var user = $('#user').val();
  var data = {
    'sender': 'user',
    'message': user
  };
  var url = "http://localhost:5005/webhooks/rest/webhook";
  $("#chats").append("<div class='user'><p>"+user+"</p></div>");
  $.ajax(url ,{
    'data': JSON.stringify(data), 
    'type': 'POST',
    'processData': false,
    'contentType': 'application/json',
    'success': function(result){
      console.log(result);
      $("#chats").append("<div class='comp'><p>"+result[0].text+"</p></div>");
      said(result[0].text);
    }
  });
  $('#user').val("");
}

function sound() {
  var recognizer = new webkitSpeechRecognition();
  recognizer.lang = "en";
  recognizer.onresult = function(event) {
    if (event.results.length > 0) {
        var result = event.results[event.results.length-1];
        if(result.isFinal) {
          $('#user').val(result[0].transcript); 
        }
    }  
  };
  recognizer.start();
}

function said(word) {
  var su = new SpeechSynthesisUtterance();
  su.lang = "en";
  su.text = word;
  speechSynthesis.speak(su);
}

$(document).ready(function() {
  $(window).keydown(function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      send();
      return false;
    }
  });
});