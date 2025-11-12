# rg_send_death_message
#### Syntax
```
native rg_send_death_message(const pKiller, const pVictim, const pAssister, const pevInflictor, const killerWeaponName[], const DeathMessageFlags:iDeathMessageFlags, const KillRarity:iRarityOfKill);
```

#### Usage
pKiller | ```Killer index (if any).```
---|---
pVictim | ```Victim index.```
pAssister | ```Assisting player index (if any).```
pevInflictor | ```Inflictor entity. 0 = world```
killerWeaponName | ```The name of the weapon used by the killer.```
iDeathMessageFlags | ```Flags indicating extra death message info, see DeathMessageFlags enum in cssdk_const.inc```
iRarityOfKill | ```An bitsums representing the rarity classification of the kill, see KillRarity enum in cssdk_const.inc```
#### Description
```
Sends death messages to all players, including info about the killer, victim, weapon used,
extra death flags, death position, assistant, and kill rarity using the CHalfLifeMultiplay::SendDeathMessage function.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.