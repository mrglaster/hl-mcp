ocket_open
[Sockets](http://127.0.0.1:8000/content/index.htm) (sockets.inc) 
Description
socket_open - Opens a new connection to hostname:port and returns its handler. 
Syntax
socket_open ( hostname[], port, protocol, &error ) 
Type
Native 
Notes
Protocol can be either SOCKET_TCP or SOCKET_UDP.   
  
Returns a socket (positive) or negative or zero on error.   
  
If there is an error, the error variable (passed by reference) will contain the code.   
  
There are four return values -   
0 - No error   
1 - Error creating socket   
2 - Could not resolve hostname   
3 - Couldn't connect to given hostname:port
