# RegisterHam
#### Syntax
```
native HamHook:RegisterHam(Ham:function, const EntityClass[], const Callback[], Post=0, bool:specialbot = false);
```

#### Usage
function | ```The function to hook.```
---|---
EntityClass | ```The entity classname to hook.```
callback | ```The forward to call.```
post | ```Whether or not to forward this in post.```
specialbot | ```Whether or not to enable support for bot without "player" classname.```
#### Description
```
Hooks the virtual table for the specified entity class.
An example would be: RegisterHam(Ham_TakeDamage, "player", "player_hurt");
Look at the Ham enum for parameter lists.
```

#### Return
```
Returns a handle to the forward.  Use EnableHamForward/DisableHamForward to toggle the forward on or off.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

