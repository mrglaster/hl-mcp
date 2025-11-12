# Functions in orpheu.inc
Function | Description  
---|---  
[OrpheuGetFunction](https://amxx-bg.info/api/orpheu/OrpheuGetFunction) | ```
Retrieves a function based on a function name
The name must be the same as the one in the file where the function is defined
```
  
[OrpheuRegisterHook](https://amxx-bg.info/api/orpheu/OrpheuRegisterHook) | ```
Hooks a function
```
  
[OrpheuUnregisterHook](https://amxx-bg.info/api/orpheu/OrpheuUnregisterHook) | ```
Unregisters a hook (stops it)
```
  
[OrpheuCall](https://amxx-bg.info/api/orpheu/OrpheuCall) | ```
Calls a function without triggering its hooks
```
  
[OrpheuCallSuper](https://amxx-bg.info/api/orpheu/OrpheuCallSuper) | ```
Calls a function and triggers its hooks
```
  
[OrpheuGetReturn](https://amxx-bg.info/api/orpheu/OrpheuGetReturn) | ```
Gets the return value of a function (To be used in hooks Post)
```
  
[OrpheuSetReturn](https://amxx-bg.info/api/orpheu/OrpheuSetReturn) | ```
Sets the return value of a function
```
  
[OrpheuSetParam](https://amxx-bg.info/api/orpheu/OrpheuSetParam) | ```
Sets the value of an argument
```
  
[OrpheuCreateStruct](https://amxx-bg.info/api/orpheu/OrpheuCreateStruct) | ```
Creates a struct
```
  
[OrpheuGetParamStructMember](https://amxx-bg.info/api/orpheu/OrpheuGetParamStructMember) | ```
Retrieves the value of a member of a struct given the argument number the struct is and the member name
```
  
[OrpheuSetParamStructMember](https://amxx-bg.info/api/orpheu/OrpheuSetParamStructMember) | ```
Sets the value of member of a struct given the argument number the struct is and the member name
```
  
[OrpheuGetStructFromParam](https://amxx-bg.info/api/orpheu/OrpheuGetStructFromParam) | ```
Gets a struct handler for a struct received as an argument
Beware that if the original struct gets destroyed or changed these effects will reflect on your use of it.
```
  
[OrpheuCloneStructFromParam](https://amxx-bg.info/api/orpheu/OrpheuCloneStructFromParam) | ```
Creates a struct equal to one received as an argument
```
  
[OrpheuSetStructMember](https://amxx-bg.info/api/orpheu/OrpheuSetStructMember) | ```
Sets the value of a member of a struct given a struct handler and the member name
```
  
[OrpheuGetStructMember](https://amxx-bg.info/api/orpheu/OrpheuGetStructMember) | ```
Retrieves the value of a member of a struct given a struct handler and the member name
```
  
[OrpheuGetEngineFunctionsStruct](https://amxx-bg.info/api/orpheu/OrpheuGetEngineFunctionsStruct) | ```
Retrieves a handler to a struct that hold the addresses of the engine functions
By retrieving addresses from the struct is possible to hook them.
A easier way to achieve the same thing is by using the stock OrpheuGetEngineFunction
```
  
[OrpheuGetDLLFunctionsStruct](https://amxx-bg.info/api/orpheu/OrpheuGetDLLFunctionsStruct) | ```
Retrieves a handler to a struct that hold the addresses of the dll functions
By retrieving addresses from the struct is possible to hook them.
A easier way to achieve the same thing is by using the stock OrpheuGetDllFunction
```
  
[OrpheuGetFunctionFromClass](https://amxx-bg.info/api/orpheu/OrpheuGetFunctionFromClass) | ```
Retrieves a handler to a function given a classname, the function name and the classname
This function is a virtual function (a function defined in abase class and implemented
differently by each extender class)
For example: every class that extends CBaseEntity has a Spawn function. That function is defined in CBaseEntity
and implemented differently by each class derived from CBaseEntity
```
  
[OrpheuGetFunctionFromEntity](https://amxx-bg.info/api/orpheu/OrpheuGetFunctionFromEntity) | ```
Retrieves a handler to a function given the ID of an entity, the function name and the classname
This function is a virtual function (a function defined in abase class and implemented
differently by each extender class)
For example: every class that extends CBaseEntity has a Spawn function. That function is defined in CBaseEntity
and implemented differently by each class derived from CBaseEntity
```
  
[OrpheuGetFunctionFromObject](https://amxx-bg.info/api/orpheu/OrpheuGetFunctionFromObject) | ```
Retrieves a handler to a function given an object, the function name and the classname
This function is a virtual function (a function defined in abase class and implemented
differently by each extender class)
For example: every class that extends CBaseEntity has a Spawn function. That function is defined in CBaseEntity
and implemented differently by each class derived from CBaseEntity
```
  
[OrpheuGetFunctionFromMonster](https://amxx-bg.info/api/orpheu/OrpheuGetFunctionFromMonster) | ```
Retrieves a handler to a function given the id of a monster of monstermod, the function name and the classname
This function is a virtual function (a function defined in abase class and implemented
differently by each extender class)
For example: every class that extends CBaseEntity has a Spawn function. That function is defined in CBaseEntity
and implemented differently by each class derived from CBaseEntity

This function goes against the spirit of orpheu of hardcoding the less possible but without it would be much
more complex to use virtual functions
```
  

This code is a part of orpheu.inc. To use this code you should include orpheu.inc as ```#include <orpheu>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk. 