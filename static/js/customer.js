// const roomname = ""
// alert(roomname) 

var mediaDevices = navigator.mediaDevices;

$(document).ready(function(roomname ){
    var domain = "meet.jit.si";
    var options = {
        roomName: "cercoci@gmail.com",
        width: 700,
        height: 600,
        parentNode: document.querySelector('#meet')
    }
    var api = new JitsiMeetExternalAPI(domain, options);
    api.executeCommand('toggleAudio');
    api.executeCommand('toggleVideo');
});
