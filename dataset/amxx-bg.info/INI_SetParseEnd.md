# INI_SetParseEnd
#### Syntax
```
native INI_SetParseEnd(INIParser:handle, const func[]);
```

#### Usage
handle | ```Handle to an INI Parse structure.```
---|---
func | ```A ParseEnd callback.```
#### Description
```
Sets the INI_ParseEnd function of a parse handle.
```

#### Note
```
Below is the prototype of callback:
-
  Called when parsing is halted.

  @param handle        A handle to an INI Parse structure.
  @param halted        True if abnormally halted, false otherwise.
  @param data          Handle or value passed in INI_ParseFile

  @noreturn

  public OnParseEnd(INIParser:handle, bool:halted, any:data)
-
```

#### Return
```
This function has no return value.
```

#### Error
```
Invalid or corrupt handle.
```


This code is a part of textparse_ini.inc. To use this code you should include textparse_ini.inc as ```#include <textparse_ini>```


  
  

