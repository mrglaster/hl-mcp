# SMC_ParseFile
#### Syntax
```
native SMCError:SMC_ParseFile(SMCParser:handle, const file[], &line = 0, &col = 0, any:data = 0);
```

#### Usage
handle | ```A handle to an SMC Parse structure.```
---|---
file | ```A string containing the file path.```
line | ```An optional by reference cell to store the last line number read.```
col | ```An optional by reference cell to store the last column number read.```
data | ```An optional handle or value to pass through to callback functions```
#### Description
```
Parses a config file.
```

#### Return
```
An SMCParseError result.
```

#### Error
```
Invalid or corrupt handle.
```


This code is a part of textparse_smc.inc. To use this code you should include textparse_smc.inc as ```#include <textparse_smc>```


  
  

