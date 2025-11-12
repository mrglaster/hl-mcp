# GetHookChainReturn
#### Syntax
```
native any:GetHookChainReturn(AType:type, any:...);
```

#### Usage
type | ```To specify the ATYPE_* parameter, look at the enum AType```
---|---
[maxlen] | ```Max length of string (optional)```
#### Description
```
Gets the return value of the current hookchain.
This has no effect in pre hookchain.
```

#### Return
```
If an integer or boolean or one byte or float, array or everything else is passed via 1st argument and more
```


This code is a part of reapi.inc. To use this code you should include reapi.inc as ```#include <reapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.