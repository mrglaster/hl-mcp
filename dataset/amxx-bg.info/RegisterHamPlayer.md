# RegisterHamPlayer
#### Syntax
```
stock HamHook:RegisterHamPlayer(Ham:function, const Callback[], Post=0)
```

#### Usage
function | ```The function to hook.```
---|---
callback | ```The forward to call.```
post | ```Whether or not to forward this in post.```
#### Description
```
Hooks the virtual table for the player class.
An example would be: RegisterHam(Ham_TakeDamage, "player_hurt");
Look at the Ham enum for parameter lists.
```

#### Return
```
Returns a handle to the forward.  Use EnableHamForward/DisableHamForward to toggle the forward on or off.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

