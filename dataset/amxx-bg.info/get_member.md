# get_member
#### Syntax
```
native any:get_member(const index, any:member, any:...);
```

#### Usage
index | ```Entity index```
---|---
member | ```The specified member, look at the enums with name *_Members```
#### Description
```
Returns a value from an entity's member.
```

#### Return
```
If an integer or boolean or one byte, array or everything else is passed via the 3rd argument and more, look at the argument list for the specified member
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.