ocket_change
[Sockets](http://127.0.0.1:8000/content/index.htm) (sockets.inc) 
Description
socket_change - Returns true if the socket state has changed. 
Syntax
socket_change ( socket, [ timeout = 100000 ] ) 
Type
Native 
Notes
This function will return true if the state (buffer content) have changed within the last recieve or the timeout, where timeout is a value in Seconds, (1 sec = 1000000 sec). Use this to check if new data is in the socket.
