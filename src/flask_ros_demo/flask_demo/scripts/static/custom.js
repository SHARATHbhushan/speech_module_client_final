$(function () {
    //change the IP
    var ros = new ROSLIB.Ros({
        url : 'ws://192.168.192.245:9090'
    });

    ros.on('connection', function() {
        console.log('Connected to websocket server.');
    });

    ros.on('error', function(error) {
        console.log('Error connecting to websocket server: ', error);
    });

    ros.on('close', function() {
        console.log('Connection to websocket server closed.');
    });

    var listener = new ROSLIB.Topic({
        ros : ros,
        name : '/speech_recognition/final_result',
        messageType : 'std_msgs/String'
      });
    
      listener.subscribe(function(message) {
        console.log('Received message on ' + listener.name + ': ' + message.data);
        if(message.data.toLowerCase() === 'hi' || message.data.toLowerCase() === 'hello' || message.data.toLowerCase() === 'greetings' || message.data.toLowerCase() === 'how are you'){
            $("svg").toggleClass("toggle-eyes");
        setTimeout(function() {
            $("svg").toggleClass("toggle-eyes");;
          }, 5000);
        }
        if (message.data.toLowerCase() === 'very good' || message.data.toLowerCase() === 'i am impressed' || message.data.toLowerCase() === 'i love you' || message.data.toLowerCase() === 'i like you') {
            $("svg").toggleClass("toggle-heart");
            setTimeout(function() {
                $("svg").toggleClass("toggle-heart");;
              }, 5000);
        }
        if (message.data.toLowerCase() === 'how is the weather today' || message.data.toLowerCase() === 'tell me what is the temperature at home' || message.data.toLowerCase() === 'home temperature' || message.data.toLowerCase() === 'Temperature at home') {
            $("svg").toggleClass("toggle-trace-web");
            setTimeout(function() {
                $("svg").toggleClass("toggle-trace-web");;
              }, 5000);
        }
        if (message.data.toLowerCase() === 'tell me some jokes' || message.data.toLowerCase() === 'joke please' || message.data.toLowerCase() === 'any good jokes' || message.data.toLowerCase() === 'jokes') {
            $("svg").toggleClass("toggle-eyes-scan");
            setTimeout(function() {
                $("svg").toggleClass("toggle-eyes-scan");;
              }, 5000);
        }
        if (message.data.toLowerCase() === 'back in a bit' || message.data.toLowerCase() === 'see ya' || message.data.toLowerCase() === 'bye for now' || message.data.toLowerCase() === 'bye') {
            $("svg").toggleClass("toggle-terminal");
            setTimeout(function() {
                $("svg").toggleClass("toggle-terminal");;
              }, 5000);
        }
        generate_message(message.data, 'self');
        submit_message(message.data);
      });


    let INDEX = 0;
    $('#chat-submit').click(function (e) {
        e.preventDefault();
        const msg = $('#chat-input').val();
        if (msg.trim() === '') {
            return false;
        }
        if(msg.toLowerCase() === 'hi' || msg.toLowerCase() === 'hello' || msg.toLowerCase() === 'greetings' || msg.toLowerCase() === 'how are you'){
            $("svg").toggleClass("toggle-eyes");
        setTimeout(function() {
            $("svg").toggleClass("toggle-eyes");;
          }, 5000);
        }
        if (msg.toLowerCase() === 'very good' || msg.toLowerCase() === 'i am impressed' || msg.toLowerCase() === 'i love you' || msg.toLowerCase() === 'i like you') {
            $("svg").toggleClass("toggle-heart");
            setTimeout(function() {
                $("svg").toggleClass("toggle-heart");;
              }, 5000);
        }
        if (msg.toLowerCase() === 'how is the weather today' || msg.toLowerCase() === 'tell me what is the temperature at home' || msg.toLowerCase() === 'home temperature' || msg.toLowerCase() === 'Temperature at home') {
            $("svg").toggleClass("toggle-trace-web");
            setTimeout(function() {
                $("svg").toggleClass("toggle-trace-web");;
              }, 5000);
        }
        if (msg.toLowerCase() === 'tell me some jokes' || msg.toLowerCase() === 'joke please' || msg.toLowerCase() === 'any good jokes' || msg.toLowerCase() === 'jokes') {
            $("svg").toggleClass("toggle-eyes-scan");
            setTimeout(function() {
                $("svg").toggleClass("toggle-eyes-scan");;
              }, 5000);
        }
        if (msg.toLowerCase() === 'back in a bit' || msg.toLowerCase() === 'see ya' || msg.toLowerCase() === 'bye for now' || msg.toLowerCase() === 'bye') {
            $("svg").toggleClass("toggle-terminal");
            setTimeout(function() {
                $("svg").toggleClass("toggle-terminal");;
              }, 5000);
        }

        generate_message(msg, 'self');
        submit_message(msg);
    });

    //output
    function submit_message(message) {
        const sendRequest = $.post('/chat', {message: message});
        sendRequest.done(function (data) {
            console.log(data);
            var nlu_out = new ROSLIB.Topic({
                ros : ros,
                name : '/tts/phrase',
                messageType : 'std_msgs/String'
              });
            var nm =new ROSLIB.Message({
                data: data.message
            });
            nlu_out.publish(nm);
            console.log(data.message.toLowerCase())
            if (data.message.toLowerCase() === 'speak to you soon'){
                console.log("working")
                var stt_handler = new ROSLIB.Topic({
                    ros : ros,
                    name : '/stt_session_key',
                    messageType : 'std_msgs/Bool'
                  });
                var stt_state =new ROSLIB.Message({
                    data: false
                });
                stt_handler.publish(stt_state);
            }

            generate_message(data.message, 'user');
            if (data && data.payload !== null) {
                const buttons = data.payload.suggestion_chips;
                let srtButton = '';
                buttons.map((button) => (
                    srtButton += '<button type="button" class="btn btn-outline-secondary mr-1 btn-chips" onclick="$(\'#chat-input\').val(\'' + button + '\');$(\'#chat-submit\').click();">' + button + '</button>'
                ))
                generate_message(srtButton, 'button')
            }
        });

    }
    //imput
    function generate_message(msg, type) {
        const chatLogs = $('.chat-logs');
        INDEX++;
        let str = '';
        str += "<div id='cm-msg-" + INDEX + '\' class="chat-msg ' + type + '">';
        if (type !== 'button') {
            str += '<div class="cm-msg-text">';
            str += msg;
            str += '</div>';
            
        } else {
            str += '<div class="cm-msg-buttons">';
            str += msg;
            str += '</div>';
        }
        str += '</div>';
        chatLogs.append(str);
        
        //console.log(msg)

        $('#cm-msg-' + INDEX).hide().fadeIn(300);
        if (type === 'self') {
            $('#chat-input').val('');
        }
        chatLogs.stop().animate({scrollTop: chatLogs[0].scrollHeight}, 1000);
    }
    

    $(document).delegate('.chat-btn', 'click', function () {
        const value = $(this).attr('chat-value');
        const name = $(this).html();
        $('#chat-input').attr('disabled', false);
        generate_message(name, 'self');
    });

    $('#chat-circle').click(function () {
        $('#chat-circle').toggle('scale');
        $('.chat-box').toggle('scale');
    });

    $('.chat-box-toggle').click(function () {
        $('#chat-circle').toggle('scale');
        $('.chat-box').toggle('scale');
    });
    $("button.btn-terminal").click(function() {
        $("svg").toggleClass("toggle-terminal");
    });
    
    $("button.btn-heart").click(function() {
        $("svg").toggleClass("toggle-heart");
    });
    
    $("button.btn-eyes").click(function() {
        $("svg").toggleClass("toggle-eyes");
    });
    
    $("button.btn-scan").click(function() {
        $("svg").toggleClass("toggle-eyes-scan");
    });
    
    $("button.btn-web").click(function() {
        $("svg").toggleClass("toggle-trace-web");
    });
    
    $("button.btn-rotate").click(function() {
        $("svg").toggleClass("toggle-rotate");
    });
});
