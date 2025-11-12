# show_dhudmessage
#### Syntax
```
native show_dhudmessage(index, const message[], any:...);
```

#### Usage
index | ```Client index, use 0 to display to all clients```
---|---
message | ```Formatting rules```
... | ```Variable number of formatting parameters```
#### Description
```
Displays a director message on the client HUD.
```

#### Note
```
Use set_dhudmessage to define how the message should look on screen.
```

#### Note
```
Unlike the classic HUD message, which is channel-based, director
messages are stack-based. You can have up to 8 messages displaying at
once. If more are added, they will be overwritten in the order they were
sent. There is no way to clear a specific message.
```

#### Note
```
The message has a maximum length of 128 characters which this function
will automatically enforce.
```

#### Note
```
This functions return value behaves differently depending on what is
used as the client index: If 0 is specified, then the function will
return 0 if nothing has been sent (no client connected). If either a
single client is specified, or there is at least one client connected,
the number of printed characters will refer to the message that is sent
last, to the client with the highest index.
```

#### Return
```
Number of printed characters
```

#### Error
```
If a single client is specified and the index is not within
the range of 1 to MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

