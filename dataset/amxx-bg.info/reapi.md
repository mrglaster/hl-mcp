# Functions in reapi.inc
Function | Description  
---|---  
[RegisterHookChain](https://amxx-bg.info/api/reapi/RegisterHookChain) | ```
Hook API function that are available into enum.
Look at the enums for parameter lists.
```
  
[DisableHookChain](https://amxx-bg.info/api/reapi/DisableHookChain) | ```
Stops a hook from triggering.
Use the return value from RegisterHookChain as the parameter here!
```
  
[EnableHookChain](https://amxx-bg.info/api/reapi/EnableHookChain) | ```
Starts a hook back up.
Use the return value from RegisterHookChain as the parameter here!
```
  
[SetHookChainReturn](https://amxx-bg.info/api/reapi/SetHookChainReturn) | ```
Sets the return value of a hookchain.
```
  
[GetHookChainReturn](https://amxx-bg.info/api/reapi/GetHookChainReturn) | ```
Gets the return value of the current hookchain.
This has no effect in pre hookchain.
```
  
[SetHookChainArg](https://amxx-bg.info/api/reapi/SetHookChainArg) | ```
Set hookchain argument.
This has no effect in post hookchain.
```
  
[IsReapiHookOriginalWasCalled](https://amxx-bg.info/api/reapi/IsReapiHookOriginalWasCalled) | ```
Return call state of original API function (that are available into enum).
Look at the enums for parameter lists.
```
  
[GetCurrentHookChainHandle](https://amxx-bg.info/api/reapi/GetCurrentHookChainHandle) | ```
Returns the current hookchain handle.
```
  
[FClassnameIs](https://amxx-bg.info/api/reapi/FClassnameIs) | ```
Compares the entity to a specified classname.
```
  
[GetGrenadeType](https://amxx-bg.info/api/reapi/GetGrenadeType) | ```
To get WeaponIdType from grenade entity
```
  
[engset_view](https://amxx-bg.info/api/reapi/engset_view) | ```
Sets the view entity on a client.
This allows pfnSetView able to hooks.
```
  
[get_viewent](https://amxx-bg.info/api/reapi/get_viewent) | ```
Gets the return index of the current view entity on a client.
```
  
[is_entity](https://amxx-bg.info/api/reapi/is_entity) | ```
Check if the entity is valid.
```
  
[is_rehlds](https://amxx-bg.info/api/reapi/is_rehlds) | ```
Check if ReHLDS is available.
```
  
[is_regamedll](https://amxx-bg.info/api/reapi/is_regamedll) | ```
Check if ReGameDLL is available.
```
  
[has_reunion](https://amxx-bg.info/api/reapi/has_reunion) | ```
Check if Reunion is available.
```
  
[has_vtc](https://amxx-bg.info/api/reapi/has_vtc) | ```
Check if VTC is available.
```
  
[has_rechecker](https://amxx-bg.info/api/reapi/has_rechecker) | ```
Check if Rechecker is available.
```
  

This code is a part of reapi.inc. To use this code you should include reapi.inc as ```#include <reapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.