# ns_takedamage
#### Syntax
```
#pragma deprecated It is suggested to use hamsandwich for this action instead.
native ns_takedamage(IDVictim, IDInflictor, IDAttacker, Float:Damage, DamageType);
```

#### Usage
IDVictim | ```The victim that is taking the damage.```
---|---
IDInflictor | ```The entity that is causing the damage (weapon, etc).```
IDAttacker | ```The attacker who is triggering the damage (person shooting).```
Damage | ```The amount of damage being done.```
DamageType | ```The damage type being done (bitmask).```
#### Description
```
Calls NS's private damage routine on the victim entity.
```

This function is deprecated, do NOT use it!
#### Note
```
This is provided for backwards compatibility with peachy's module.
It is suggested to use hamsandwich for this action instead.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).