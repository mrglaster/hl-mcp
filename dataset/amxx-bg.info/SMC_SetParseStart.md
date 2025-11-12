# SMC_SetParseStart
#### Syntax
```
native SMC_SetParseStart(SMCParser:handle, const func[]);
```

#### Usage
handle | ```Handle to an SMC Parse structure.```
---|---
func | ```A ParseStart callback.```
#### Description
```
Sets the SMC_ParseStart function of a parse handle.
```

#### Note
```
Below is the prototype of callback:
-
  Called when parsing is started.

  @param handle        Handle to an SMC Parse structure.
  @param data          Handle or value passed in SMC_ParseFile

  @noreturn

  public OnParseStart(SMCParser:handle, any:data)
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


  
  

