# rg_death_notice
#### Syntax
```
native rg_death_notice(const pVictim, const pKiller, const pevInflictor);
```

#### Usage
pVictim | ```Player index.```
---|---
pKiller | ```Killer entity.```
pevInflictor | ```Inflictor entity. 0 = world```
#### Description
```
Emits a death notice (logs, DeathMsg event, win conditions check)
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.