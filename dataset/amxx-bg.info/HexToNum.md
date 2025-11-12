# HexToNum
#### Syntax
```
stock HexToNum(const hexstr[])
```

#### Usage
hexstr | ```HEX string to parse.```
---|---
#### Description
```
Converts string HEX representation to an integer value.
```

#### Note
```
Function converts chars in ranges 0-9, a-f, A-F. Strings are parsed up to 8 chars length.
```

#### Return
```
Integer value represeting given HEX string or 0 if HEX string contains invalid characters.
```


This code is a part of common_functions.inc. To use this code you should include common_functions.inc as ```#include <common_functions>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.