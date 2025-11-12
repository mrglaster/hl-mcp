# socket_is_readable
#### Syntax
```
native socket_is_readable(_socket, _timeout = 100000);
```

#### Usage
_socket | ```Socket descriptor```
---|---
_timeout | ```Amount of time to block the call waiting for the socket to be marked as readable or for the timeout to expire, in µSeconds (1 sec = 1000000 µsec)```
#### Description
```
Checks if a socket is marked as readable.
```

#### Note
```
You can use this function to make sure there's something on the socket and avoid a blocking call.
```

#### Note
```
Set _timeout to 0 avoid blocking the call.
```

#### Note
```
A socket will become readable if there's any data or an EOF.
```

#### Return
```
1 if the socket is marked as readable
0 otherwise
```


This code is a part of sockets.inc. To use this code you should include sockets.inc as ```#include <sockets>```


  
  

