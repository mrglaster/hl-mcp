# RegisterQueryFile
#### Syntax
```
native QueryFileHook:RegisterQueryFile(const file[], const function[], const ResourceType:type, const hash = -1);
```

#### Usage
file | ```The file (Can contain a relative path to the file)```
---|---
function | ```The forward to call```
type | ```The request type, can be only RES_TYPE_EXISTS, RES_TYPE_MISSING or RES_TYPE_HASH_ANY```
hash | ```Hash of file to request.```
#### Description
```
Send request the file for the client to get hash
```

#### Return
```
Returns a hook handle. Use UnRegisterQueryFile to remove the forward
```


This code is a part of reapi_rechecker.inc. To use this code you should include reapi_rechecker.inc as ```#include <reapi_rechecker>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReChecker Metamod Plugin for correct work