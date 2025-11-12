# socket_open
#### Syntax
```
native socket_open(const _hostname[], _port, _protocol = SOCKET_TCP, &_error, _flags = 0);
```

#### Usage
_hostname | ```Node to connect to```
---|---
_port | ```Service to connect to```
_protocol | ```Connect via SOCKET_TCP or SOCKET_UDP```
_error | ```Set an error code here if anything goes wrong```
_flags | ```Optional bit flags that change the behaviour of the function```
#### Description
```
Connects to the given node and service via TCP/UDP.
```

#### Note
```
There's 2 types of error reporting on this function that you can use.
```

#### Note
```
Default error codes:
0 - No error
1 - Error while creating socket
2 - Couldn't resolve hostname
3 - Couldn't connect
```

#### Note
```
New, more expressive libc error codes:
https://www.gnu.org/software/libc/manual/html_node/Error-Codes.html
https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/errno.h
https://msdn.microsoft.com/en-us/library/ms740668.aspx
```

#### Note
```
The currently available bit flags are:
- SOCK_NON_BLOCKING : if set, the socket will be on nonblocking mode
- SOCK_LIBC_ERRORS : if set, the new libc errors will be seen on _error
```

#### Note
```
If no flags are set, the behaviour of the function will not be modified.
```

#### Note
```
Multiple flags may be set at the same time using the | operator.
For example, SOCK_NON_BLOCKING|SOCK_LIBC_ERRORS will create a nonblocking socket with libc error codes.
```

#### Note
```
If you're creating a new nonblocking socket, _hostname should be numeric to avoid calling the
name resolution server and potentially blocking the call.
```

#### Note
```
If the socket is a nonblocking one, the returned socket descriptor may be still connecting and
further checks should be done with socket_is_writable() before trying to send data.
```

#### Return
```
A socket descriptor (a positive integer) on success
-1 on failure
```


This code is a part of sockets.inc. To use this code you should include sockets.inc as ```#include <sockets>```


  
  

