# Functions in hamsandwich.inc
Function | Description  
---|---  
[RegisterHam](https://amxx-bg.info/api/hamsandwich/RegisterHam) | ```
Hooks the virtual table for the specified entity class.
An example would be: RegisterHam(Ham_TakeDamage, "player", "player_hurt");
Look at the Ham enum for parameter lists.
```
  
[RegisterHamPlayer](https://amxx-bg.info/api/hamsandwich/RegisterHamPlayer) | ```
Hooks the virtual table for the player class.
An example would be: RegisterHam(Ham_TakeDamage, "player_hurt");
Look at the Ham enum for parameter lists.
```
  
[RegisterHamFromEntity](https://amxx-bg.info/api/hamsandwich/RegisterHamFromEntity) | ```
Hooks the virtual table for the specified entity's class.
An example would be: RegisterHam(Ham_TakeDamage, id, "player_hurt");
Look at the Ham enum for parameter lists.
Note: This will cause hooks for the entire internal class that the entity is
      not exclusively for the provided entity.
```
  
[DisableHamForward](https://amxx-bg.info/api/hamsandwich/DisableHamForward) | ```
Stops a ham forward from triggering.
Use the return value from RegisterHam as the parameter here!
```
  
[EnableHamForward](https://amxx-bg.info/api/hamsandwich/EnableHamForward) | ```
Starts a ham forward back up.
Use the return value from RegisterHam as the parameter here!
```
  
[ExecuteHam](https://amxx-bg.info/api/hamsandwich/ExecuteHam) | ```
Executes the virtual function on the entity.
Look at the Ham enum for parameter lists.
```
  
[ExecuteHamB](https://amxx-bg.info/api/hamsandwich/ExecuteHamB) | ```
Executes the virtual function on the entity, this will trigger all hooks on that function.
Be very careful about recursion!
Look at the Ham enum for parameter lists.
```
  
[GetHamReturnStatus](https://amxx-bg.info/api/hamsandwich/GetHamReturnStatus) | ```
Gets the return status of the current hook.
This is useful to determine what return natives to use.
```
  
[GetHamReturnInteger](https://amxx-bg.info/api/hamsandwich/GetHamReturnInteger) | ```
Gets the return value of a hook for hooks that return integers or booleans.
```
  
[GetHamReturnFloat](https://amxx-bg.info/api/hamsandwich/GetHamReturnFloat) | ```
Gets the return value of a hook for hooks that return float.
```
  
[GetHamReturnVector](https://amxx-bg.info/api/hamsandwich/GetHamReturnVector) | ```
Gets the return value of a hook for hooks that return Vectors.
```
  
[GetHamReturnEntity](https://amxx-bg.info/api/hamsandwich/GetHamReturnEntity) | ```
Gets the return value of a hook for hooks that return entities.
```
  
[GetHamReturnString](https://amxx-bg.info/api/hamsandwich/GetHamReturnString) | ```
Gets the return value of a hook for hooks that return strings.
```
  
[GetOrigHamReturnInteger](https://amxx-bg.info/api/hamsandwich/GetOrigHamReturnInteger) | ```
Gets the original return value of a hook for hooks that return integers or booleans.
```
  
[GetOrigHamReturnFloat](https://amxx-bg.info/api/hamsandwich/GetOrigHamReturnFloat) | ```
Gets the original return value of a hook for hooks that return floats.
```
  
[GetOrigHamReturnVector](https://amxx-bg.info/api/hamsandwich/GetOrigHamReturnVector) | ```
Gets the original return value of a hook for hooks that return Vectors.
```
  
[GetOrigHamReturnEntity](https://amxx-bg.info/api/hamsandwich/GetOrigHamReturnEntity) | ```
Gets the original return value of a hook for hooks that return entities.
```
  
[GetOrigHamReturnString](https://amxx-bg.info/api/hamsandwich/GetOrigHamReturnString) | ```
Gets the original return value of a hook for hooks that return strings.
```
  
[SetHamReturnInteger](https://amxx-bg.info/api/hamsandwich/SetHamReturnInteger) | ```
Sets the return value of a hook that returns an integer or boolean.
This needs to be used in conjunction with HAM_OVERRIDE or HAM_SUPERCEDE.
```
  
[SetHamReturnFloat](https://amxx-bg.info/api/hamsandwich/SetHamReturnFloat) | ```
Sets the return value of a hook that returns a float.
This needs to be used in conjunction with HAM_OVERRIDE or HAM_SUPERCEDE.
```
  
[SetHamReturnVector](https://amxx-bg.info/api/hamsandwich/SetHamReturnVector) | ```
Sets the return value of a hook that returns a Vector.
This needs to be used in conjunction with HAM_OVERRIDE or HAM_SUPERCEDE.
```
  
[SetHamReturnEntity](https://amxx-bg.info/api/hamsandwich/SetHamReturnEntity) | ```
Sets the return value of a hook that returns an entity.  Set to -1 for null.
This needs to be used in conjunction with HAM_OVERRIDE or HAM_SUPERCEDE.
```
  
[SetHamReturnString](https://amxx-bg.info/api/hamsandwich/SetHamReturnString) | ```
Sets the return value of a hook that returns a string.
This needs to be used in conjunction with HAM_OVERRIDE or HAM_SUPERCEDE.
```
  
[SetHamParamInteger](https://amxx-bg.info/api/hamsandwich/SetHamParamInteger) | ```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are integers.
```
  
[SetHamParamFloat](https://amxx-bg.info/api/hamsandwich/SetHamParamFloat) | ```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are floats.
```
  
[SetHamParamVector](https://amxx-bg.info/api/hamsandwich/SetHamParamVector) | ```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are Vectors.
```
  
[SetHamParamEntity](https://amxx-bg.info/api/hamsandwich/SetHamParamEntity) | ```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are entities.
```
  
[SetHamParamEntity2](https://amxx-bg.info/api/hamsandwich/SetHamParamEntity2) | ```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are entities.
```
  
[SetHamParamString](https://amxx-bg.info/api/hamsandwich/SetHamParamString) | ```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are strings.
```
  
[SetHamParamTraceResult](https://amxx-bg.info/api/hamsandwich/SetHamParamTraceResult) | ```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are trace result handles.
```
  
[SetHamParamItemInfo](https://amxx-bg.info/api/hamsandwich/SetHamParamItemInfo) | ```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are trace result handles.
```
  
[GetHamItemInfo](https://amxx-bg.info/api/hamsandwich/GetHamItemInfo) | ```
Gets a parameter on the fly of the current hook.
Use this on parameters that are iteminfo result handles.
```
  
[SetHamItemInfo](https://amxx-bg.info/api/hamsandwich/SetHamItemInfo) | ```
Sets a parameter on the fly of the current hook.
Use this on parameters that are iteminfo result handles.
```
  
[CreateHamItemInfo](https://amxx-bg.info/api/hamsandwich/CreateHamItemInfo) | ```
Creates an ItemInfo handle.  This value should never be altered.
The handle can be used in Get/SetHamItemInfo.

NOTE: You must call FreeHamItemInfo() on every handle made with CreateHamItemInfo().
```
  
[FreeHamItemInfo](https://amxx-bg.info/api/hamsandwich/FreeHamItemInfo) | ```
Frees an ItemIndo handle created with CreateHamItemInfo().  Do not call
this more than once per handle, or on handles not created through
CreateHamItemInfo().
```
  
[IsHamValid](https://amxx-bg.info/api/hamsandwich/IsHamValid) | ```
Returns whether or not the function for the specified Ham is valid.
Things that would make it invalid would be bounds (an older module version
 may not have all of the functions), and the function not being found in
 the mod's hamdata.ini file.
```
  
[get_pdata_cbase](https://amxx-bg.info/api/hamsandwich/get_pdata_cbase) | ```
This is used to compliment fakemeta's {get,set}_pdata_{int,float,string}.
This requires the mod to have the pev and base fields set in hamdata.ini.
Note this dereferences memory! Improper use of this will crash the server.
This will return an index of the corresponding cbase field in private data.
Returns -1 on a null entry.
```
  
[set_pdata_cbase](https://amxx-bg.info/api/hamsandwich/set_pdata_cbase) | ```
This is used to compliment fakemeta's {get,set}_pdata_{int,float,string}.
This requires the mod to have the pev and base fields set in hamdata.ini.
This will set the corresponding cbase field in private data with the index.
Pass -1 to null the entry.
```
  
[get_pdata_cbase_safe](https://amxx-bg.info/api/hamsandwich/get_pdata_cbase_safe) | ```
This is similar to the get_pdata_cbase, however it does not dereference memory.
This is many times slower than get_pdata_cbase, and this should only be used
for testing and finding of offsets, not actual release quality plugins.
This will return an index of the corresponding cbase field in private data.
Returns -1 on a null entry. -2 on an invalid entry.
```
  

This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

