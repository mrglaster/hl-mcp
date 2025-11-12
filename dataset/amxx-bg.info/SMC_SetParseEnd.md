# SMC_SetParseEnd
#### Syntax
```
native SMC_SetParseEnd(SMCParser:handle, const func[]);
```

#### Usage
handle | ```Handle to an SMC Parse structure.```
---|---
func | ```A ParseEnd callback.```
#### Description
```
Sets the SMC_ParseEnd function of a parse handle.
```

#### Note
```
Below is the prototype of callback:
-
  Called when parsing is halted.

  @param handle        Handle to an SMC Parse structure.
  @param halted        True if abnormally halted, false otherwise.
  @param failed        True if parsing failed, false otherwise.
  @param data          Handle or value passed in SMC_ParseFile

  @noreturn

  public OnParseEnd(SMCParser:handle, bool:halted, bool:failed, any:data)
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


This code is a part of textparse_smc.inc. To use this code you should include textparse_smc.inc as ```#include <textparse_smc>```


  
  

