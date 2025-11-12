# SMC_SetRawLine
#### Syntax
```
native SMC_SetRawLine(SMCParser:handle, const func[]);
```

#### Usage
handle | ```Handle to an SMC Parse structure.```
---|---
func | ```A RawLine callback.```
#### Description
```
Sets a raw line reader on an text parser handle.
```

#### Note
```
Below is the prototype of callbacks:
-
  Called whenever a raw line is read.

  @param handle        Handle to an SMC Parse structure.
  @param line          A string containing the raw line from the file.
  @param lineno        The line number it occurs on.
  @param data          Handle or value passed in SMC_ParseFile

  @return              An SMCResult action to take.

  public SMCResult:SMC_RawLine(SMCParser:handle, const line[], lineno, any:data)
-
```

#### Return
```
This function has no return value.
```


This code is a part of textparse_smc.inc. To use this code you should include textparse_smc.inc as ```#include <textparse_smc>```


  
  

