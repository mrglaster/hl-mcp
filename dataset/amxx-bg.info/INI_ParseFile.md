# INI_ParseFile
#### Syntax
```
native bool:INI_ParseFile(INIParser:handle, const file[], &line = 0, &col = 0, any:data = 0);
```

#### Usage
handle | ```A handle to an INI Parse structure.```
---|---
file | ```A string containing the file path.```
line | ```An optional by reference cell to store the last line number read.```
col | ```An optional by reference cell to store the last column number read.```
data | ```An optional handle or value to pass through to callback functions```
#### Description
```
Parses an INI config file.
```

#### Return
```
An SMCParseError result.
```

#### Error
```
Invalid or corrupt handle.
```


This code is a part of textparse_ini.inc. To use this code you should include textparse_ini.inc as ```#include <textparse_ini>```


  
  

