# rg_fire_buckshots
#### Syntax
```
native rg_fire_buckshots(const inflictor, const attacker, const shots, Float:vecSrc[3], Float:vecDirShooting[3], Float:vecSpread[3], const Float:flDistance, const iTracerFreq, const iDamage);
```

#### Usage
inflictor | ```Inflictor is the entity that caused the damage (such as a gun)```
---|---
attacker | ```Attacker is the entity that triggered the damage (such as the gun's owner)```
shots | ```The number of shots```
vecSrc | ```The source position of the barrel```
vecDirShooting | ```Shooting direction```
vecSpread | ```Spread```
flDistance | ```Max shot distance```
iTracerFreq | ```Tracer frequency```
iDamage | ```Damage amount```
#### Description
```
Fires buckshots from entity (used at XM1014 and M3 weapons).
```

#### Note
```
: This native doesn't create a decal effect
```

#### Note
```
: Decal creation is handled by PlaybackEvent, including shot animation and shot sound
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.