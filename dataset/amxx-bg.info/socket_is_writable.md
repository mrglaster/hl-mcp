# socket_is_writable
#### Syntax
```
native socket_is_writable(_socket, _timeout = 100000);
```

#### Usage
_socket | ```Socket descriptor```
---|---
_timeout | ```Amount of time to block the call waiting for the socket to be marked as writable or for the timeout to expire, in µSeconds (1 sec = 1000000 µsec)```
#### Description
```
Checks if a socket is marked as writable.
```

#### Note
```
Use this function to check if a nonblocking socket is ready to be used.
```

#### Note
```
Set _timeout to 0 avoid blocking the call.
```

#### Note
```
An UDP socket is always writable.
```

#### Return
```
1 if the socket is marked as writable
0 otherwise
```


This code is a part of sockets.inc. To use this code you should include sockets.inc as ```#include <sockets>```


  
  

