# SetTouch
#### Syntax
```
native SetTouch(const ent, const callback[], const params[] = "", const len = 0);
```

#### Usage
entity | ```Entity index```
---|---
callback | ```The forward to call```
params | ```Optional set of data to pass through to callback```
len | ```Optional size of data```
#### Description
```
Sets Touch callback for entity
```

#### Note
```
Use "" to reset callback
```

#### Note
```
Callback should be contains passing arguments as "public Touch_Callback(const ent, const other)"
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.