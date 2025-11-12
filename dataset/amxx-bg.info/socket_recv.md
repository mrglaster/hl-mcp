# socket_recv
#### Syntax
```
native socket_recv(_socket, _data[], _length);
```

#### Usage
_socket | ```Socket descriptor```
---|---
_data | ```Array to save the data```
_length | ```Length of the array```
#### Description
```
Receives data.
```

#### Note
```
The amount of bytes than you end up receiving can be less than the one you expected.
```

#### Note
```
This function will completely block the server until some data arrives
to the given socket. Use this only if you are sure there is some data
to be retrieved. You can do that by polling with socket_is_readable().
```

#### Return
```
Amount of bytes received
0 if the peer closed the connection
-1 on failure
```


This code is a part of sockets.inc. To use this code you should include sockets.inc as ```#include <sockets>```


  
  

