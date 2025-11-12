# SMC_GetErrorString
#### Syntax
```
native bool:SMC_GetErrorString(SMCError:error, buffer[], buf_max);
```

#### Usage
error | ```The SMCParseError code.```
---|---
buffer | ```A string buffer for the error (contents undefined on failure).```
buf_max | ```The maximum size of the buffer.```
#### Description
```
Gets an error string for an SMCError code.
```

#### Note
```
SMCError_Okay returns false.
```

#### Note
```
SMCError_Custom (which is thrown on SMCParse_HaltFail) returns false.
```

#### Return
```
True on success, false otherwise.
```


This code is a part of textparse_smc.inc. To use this code you should include textparse_smc.inc as ```#include <textparse_smc>```


  
  

