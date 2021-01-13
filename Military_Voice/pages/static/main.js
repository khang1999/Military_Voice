$('.tablinks').click(function() {

	$('.tabcontent').css('display', 'none')

	// $('#Speak').css('display', 'block')
	$('#' + $(this).data('target')).css('display', 'block')

	$('.tablinks').removeClass('active')

	$(this).addClass('active')

})

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})


var speakIndex = Math.floor(Math.random() * sentences.length)
if(speakIndex > 0){
    $('.card-speak-text').text(sentences[speakIndex].text)
}

var listenIndex = Math.floor(Math.random() * recordings.length)


if(listenIndex > 0){
    if(!recordings[listenIndex].verified){
        $('.card-listen-text').text(recordings[listenIndex].text)
        var audioObject = $('<audio controls></audio>')
            .attr('src', recordings[listenIndex].audiofile);
        $('div[data-role="recordings-listen"] .row').append(audioObject)
    }
}

$('.btn-validate-yes').click(function() {
    var fd = new FormData();
    fd.append('id', recordings[listenIndex].id)
    // fd.append('audiofile', recordings[listenIndex].audiofile)
    // fd.append('textid', recordings[listenIndex].id)
    // fd.append('text', recordings[listenIndex].text)
    fd.append('verified', 1)

    $.ajax({
        type: 'POST',
        url: '/home/speak/',
        data: fd,
        processData: false,
        contentType: false
    }).done(function(response) {
        console.log(response)
    })

    location.reload()

})


$('.btn-validate-no').click(function() {
    var fd = new FormData();
    fd.append('id', recordings[listenIndex].id)
    fd.append('verified', 2)

    $.ajax({
        type: 'POST',
        url: '/home/speak/',
        data: fd,
        processData: false,
        contentType: false
    }).done(function(response) {
        console.log(response)
    })
    location.reload()
})


var recordingLength = recordings.length
var sentenceLength = sentences.length * 10

const progress = document.querySelector('.progress-bar')

if(progress != null){
    setTimeout(() => {
        progress.style.opacity = 1
        progress.style.width = ((recordingLength/sentenceLength) * 100) + '%'
    }, 500)
}

$('.speak-progress').text('Progress: ' + recordingLength + '/' + sentenceLength)
$('.counter').text(recordingLength + '/' + sentenceLength)


function blobToFile(theBlob, fileName){
    //A Blob() is almost a File() - it's just missing the two properties below which we will add
    theBlob.lastModifiedDate = new Date();
    theBlob.name = fileName;
    return theBlob;
}

jQuery(document).ready(function () {
    var $ = jQuery;
    var myRecorder = {
        objects: {
            context: null,
            stream: null,
            recorder: null
        },
        init: function () {
            if (null === myRecorder.objects.context) {
                myRecorder.objects.context = new (
                        window.AudioContext || window.webkitAudioContext
                        );
            }
        },
        start: function () {
            var options = {audio: true, video: false};
            navigator.mediaDevices.getUserMedia(options).then(function (stream) {
                myRecorder.objects.stream = stream;
                myRecorder.objects.recorder = new Recorder(
                        myRecorder.objects.context.createMediaStreamSource(stream),
                        {numChannels: 1}
                );
                myRecorder.objects.recorder.record();
            }).catch(function (err) {});
        },
        stop: function (listObject) {
            if (null !== myRecorder.objects.stream) {
                myRecorder.objects.stream.getAudioTracks()[0].stop();
            }
            if (null !== myRecorder.objects.recorder) {
                myRecorder.objects.recorder.stop();

                // Validate object
                if (null !== listObject
                        && 'object' === typeof listObject
                        && listObject.length > 0) {
                    // Export the WAV file
                    myRecorder.objects.recorder.exportWAV(function (blob) {
                        var url = (window.URL || window.webkitURL)
                                .createObjectURL(blob);
                        		

                        // Prepare the playback
                        var audioObject = $('<audio controls></audio>')
                                .attr('src', url);

                        var downloadObject = $('<a>Submit</a>')
                        downloadObject.click(function() {
                            let data = {'filename': new Date().toUTCString() + '.wav',
                                        'audiofile': blob,
                                        'textid': speakIndex,
                                        'text': sentences[speakIndex].text
                                        }

                            var fd = new FormData();
                            fd.append('filename', new Date().toUTCString() + '.wav')
                            fd.append('audiofile', blob)
                            fd.append('textid', speakIndex)
                            fd.append('text', sentences[speakIndex].text)
                            fd.append('verified', 0)

                            $.ajax({
                                type: 'POST',
                                url: '/home/speak/',
                                data: fd,
                                processData: false,
                                contentType: false
                            }).done(function(response) {
                                console.log(response)
                            })

                        })

                        var holderObject = $('<div class="row"></div>')
                                .append(audioObject)
                                .append(downloadObject);

                        // Append to the list
                        listObject.append(holderObject);
                    });
                }
            }
        }
    };

    // Prepare the recordings list
    var listObject = $('[data-role="recordings"]');

    // Prepare the record button
    $('[data-role="controls"] > button').click(function () {
        // Initialize the recorder
        myRecorder.init();

        // Get the button state 
        var buttonState = !!$(this).attr('data-recording');

        // Toggle
        if (!buttonState) {
            $(this).attr('data-recording', 'true');
            myRecorder.start();
        } else {
            $(this).attr('data-recording', '');
            myRecorder.stop(listObject);
        }
    });

});


var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var width = 10;
    var id = setInterval(frame, 10);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
        elem.innerHTML = width + "%";
      }
    }
  }
} 

