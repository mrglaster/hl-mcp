# socket_send
#### Syntax
```
native socket_send(_socket, const _data[], _length);
```

#### Usage
_socket | ```Socket descriptor```
---|---
_data | ```Array with the data to send```
_length | ```Length of the array```
#### Description
```
Sends data.
```

#### Note
```
The amount of bytes that end up being sent may be lower than the total length of the array,
check the return value and send the rest if needed.
```

#### Return
```
Amount of bytes sent
-1 on failure
```


This code is a part of sockets.inc. To use this code you should include sockets.inc as ```#include <sockets>```


  
  

