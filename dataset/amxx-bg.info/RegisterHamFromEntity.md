# RegisterHamFromEntity
#### Syntax
```
native HamHook:RegisterHamFromEntity(Ham:function, EntityId, const Callback[], Post=0);
```

#### Usage
function | ```The function to hook.```
---|---
EntityId | ```The entity classname to hook.```
callback | ```The forward to call.```
post | ```Whether or not to forward this in post.```
#### Description
```
Hooks the virtual table for the specified entity's class.
An example would be: RegisterHam(Ham_TakeDamage, id, "player_hurt");
Look at the Ham enum for parameter lists.
Note: This will cause hooks for the entire internal class that the entity is
      not exclusively for the provided entity.
```

#### Return
```
Returns a handle to the forward.  Use EnableHamForward/DisableHamForward to toggle the forward on or off.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

