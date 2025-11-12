# radius_damage
#### Syntax
```
native radius_damage(const Float:fExplodeAt[3], iDamageMultiplier, iRadiusMultiplier);
```

#### Usage
fExplodeAt | ```Center origin of sphere```
---|---
iDamageMultiplier | ```Damage multiplier```
iRadiusMultiplier | ```Sphere radius```
#### Description
```
Hurts (and kills, if applicable) players in a sphere.
```

#### Note
```
Players that have the DAMAGE_NO flag set in EV_INT_flags will be
ignored.
```

#### Note
```
The sphere has four different damage zones. Below is pseudo-code of the
algorithm, indicating how damage will be dealt to players:
if (distance <= 5 * radius) damage(10 + random(1 * dmg_multi))
if (distance <= 4 * radius) damage(25 + random(2 * dmg_multi))
if (distance <= 3 * radius) damage(50 + random(3 * dmg_multi))
if (distance <= 2 * radius) kill()
```

#### Return
```
This function has no return value.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

