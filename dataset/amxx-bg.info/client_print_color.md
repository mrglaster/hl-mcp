# client_print_color
#### Syntax
```
native client_print_color(index, sender, const message[], any:...);
```

#### Usage
index | ```Client index, use 0 to display to all clients```
---|---
sender | ```Client index used as the message sender```
fmt | ```Formatting rules```
... | ```Variable number of formatting parameters```
#### Description
```
Sends colored chat messages to clients.
```

#### Note
```
This only works in Counter-Strike 1.6 and Condition Zero.
```

#### Note
```
The colors can be modified inside of the format string using special
characters. These characters can be included using the escape character
   green           x04   ; use location color from this point forward
   red/blue/grey   x03   ; use team color from this point forward
   red/blue/grey   x02   ; use team color to the end of the client name
                         ; This only works at the start of the string,
                         ; and precludes using other control characters
   default         x01   ; use default color from this point forward
```

#### Note
```
The team color is defined by the sender's index. Alternatively, a
specific team color can be enforced using the print_team_* constants in
amxconst.inc
```

#### Note
```
Usage examples:
client_print_color(id, print_team_red, "^4Green ^3Red ^1Default")
client_print_color(id, id2, "^4Green ^3id2's team color, ^1Default")
```

#### Note
```
Including colors in ML can be done using the same escaping method:
EXAMPLE_ML_KEY = ^4Green ^3Team color ^1Default
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


  
  

