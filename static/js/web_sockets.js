var ws = new WebSocket("ws://127.0.0.1:8003/"),
	clock = document.getElementsByClassName('clock')[0];

ws.onmessage = function(event){
	clock.textContent = event.data;
};
