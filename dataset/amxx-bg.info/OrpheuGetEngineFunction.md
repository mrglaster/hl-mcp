# OrpheuGetEngineFunction
#### Syntax
```
stock OrpheuFunction:OrpheuGetEngineFunction(const memberName[],const libFunctionName[])
```

#### Usage
memberName | ```The name of the member of the struct that holds the address of the function Example: pfnPrecacheModel The struct representation can be seen in hlsdk at multiplayer/engine/eiface.h with the name "enginefuncs_s"```
---|---
libFunctionName | ```The name of the function as it is in the file where the function is defined```
#### Description
```
Retrieves an engine function handler by having its name as a member of the struct that hold
engine functions and the name that you give it in the file where you define the function
 The name must be the same as the one in the file where the function is defined
```

#### Return
```
A handler to the function
```


This code is a part of orpheu_stocks.inc. To use this code you should include orpheu_stocks.inc as ```#include <orpheu_stocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk.