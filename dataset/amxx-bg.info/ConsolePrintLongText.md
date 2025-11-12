# ConsolePrintLongText
#### Syntax
```
stock ConsolePrintLongText(id, text[])
```

#### Usage
id | ```The index of the player or 0 for the server.```
---|---
text | ```Multi-line text to output. No max limit for the server, but has some limits for printing to the client console.```
#### Description
```
Outputs long multi-line text in client or server console (it splits text into small chunks or lines).
```

#### Note
```
Function doesn't has any limit on text size, but take into account that printing to the client console
has limits on the network buffer.
```

#### Return
```
This function has no return value.
```


This code is a part of common_functions.inc. To use this code you should include common_functions.inc as ```#include <common_functions>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.