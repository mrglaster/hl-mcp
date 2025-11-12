# INI_SetRawLine
#### Syntax
```
native INI_SetRawLine(INIParser:handle, const func[]);
```

#### Usage
handle | ```Handle to an INI Parse structure.```
---|---
func | ```A RawLine callback.```
#### Description
```
Sets a raw line reader on an INI parser handle.
```

#### Note
```
Below is the prototype of callback:
-
  Called whenever a raw line is read.

  @param handle       The INI Parse handle.
  @param line         Contents of line.
  @param lineno       The line number it occurs on.
  @param curtok       Pointer to optionally store failed position in string.
  @param data         Handle or value passed in INI_ParseFile

  @return             True to keep parsing, false otherwise.

  public bool:OnRawLine(INIParser:smc, const line[], lineno, curtok, any:data)
```

#### Return
```
This function has no return value.
```


This code is a part of textparse_ini.inc. To use this code you should include textparse_ini.inc as ```#include <textparse_ini>```


  
  

