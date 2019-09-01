const socket = io();

socket.on('connect', function() {
  console.log('connect')
});
socket.on('disconnect', function() {
  console.log('disconnect')
});

export default socket
