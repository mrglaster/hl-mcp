# RegisterHookChain
#### Syntax
```
native HookChain:RegisterHookChain(ReAPIFunc:function_id, const callback[], post = 0);
```

#### Usage
function | ```The function to hook```
---|---
callback | ```The forward to call```
post | ```Whether or not to forward this in post```
#### Description
```
Hook API function that are available into enum.
Look at the enums for parameter lists.
```

#### Return
```
Returns a hook handle. Use EnableHookChain/DisableHookChain to toggle the forward on or off
```


This code is a part of reapi.inc. To use this code you should include reapi.inc as ```#include <reapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.