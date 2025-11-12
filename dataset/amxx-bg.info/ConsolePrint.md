# ConsolePrint
#### Syntax
```
stock ConsolePrint(id, const fmt[], any:...)
```

#### Usage
id | ```The index of the player or 0 for the server who changed.```
---|---
fmt | ```Format string.```
... | ```Parameters for format string.```
#### Description
```
Prints text to the client or server console.
```

#### Note
```
Function avoids text limits in console_print.
```

#### Note
```
Function has ability to format string, but also has limit on maximum size after formatting.
```

#### Return
```
This function has no return value.
```


This code is a part of common_functions.inc. To use this code you should include common_functions.inc as ```#include <common_functions>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.