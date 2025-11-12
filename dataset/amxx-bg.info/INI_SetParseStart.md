# INI_SetParseStart
#### Syntax
```
native INI_SetParseStart(INIParser:handle, const func[]);
```

#### Usage
handle | ```Handle to an INI Parse structure.```
---|---
func | ```A ParseStart callback.```
#### Description
```
Sets the INI_ParseStart function of a parse handle.
```

#### Note
```
Below is the prototype of callback:
-
  Called when parsing is started.

  @param handle        A handle to an INI Parse structure.
  @param data          Handle or value passed in INI_ParseFile

  @noreturn

  public OnParseStart(INIParser:handle, any:data)
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


  
  

