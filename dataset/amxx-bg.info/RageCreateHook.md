# RageCreateHook
#### Syntax
```
native RageHook:RageCreateHook(RageFunc:function,const hookFunctionName[],RageHookPhase:phase = RageHookPre)
```

#### Usage
function | ```A handler to the function```
---|---
hookFunctionName | ```The function name in the plugin that shall be called upon interception of the original function```
phase | ```The phase of the hook. It can have two values. Pre means "right before the original function is called". Post means "right after the original function is called"```
#### Description
```
Hooks a function
```

#### Return
```
A handler to the hook
```


This code is a part of rage.inc. To use this code you should include rage.inc as ```#include <rage>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.