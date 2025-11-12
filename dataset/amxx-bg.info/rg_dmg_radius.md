# rg_dmg_radius
#### Syntax
```
native rg_dmg_radius(Float:vecSrc[3], const inflictor, const attacker, const Float:flDamage, const Float:flRadius, const iClassIgnore, const bitsDamageType);
```

#### Usage
vecSrc | ```The source position```
---|---
inflictor | ```Inflictor is the entity that caused the damage (such as a gun)```
attacker | ```Attacker is the entity that triggered the damage (such as the gun's owner)```
flDamage | ```The amount of damage```
flRadius | ```Damage radius```
iClassIgnore | ```To specify classes that are immune to damage```
bitsDamageType | ```Damage type DMG_*```
#### Description
```
Inflicts damage in a radius from the source position.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.