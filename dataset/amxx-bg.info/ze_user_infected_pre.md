# ze_user_infected_pre
#### Syntax
```
forward ze_user_infected_pre(iVictim, iInfector, iDamage);
```

#### Usage
iVictim | ```Victim index, human who will catch the infection.```
---|---
iInfector | ```Infector index, zombie who will cause the infection.```
iDamage | ```The blocked damage value.```
#### Description
```
Description:     Called before user get infected by player.
```

#### Return
```
To stop the infection event use:   return ZE_STOP
To let the infection continue use: return ZE_CONTINUE
```

#### Note
```
This forward will not called on the zombie choose by the server,
only called if player try to infect player.
You can use pre to block the infection or to let it in specific conditions.
Basically return > ZE_CONTINUE  will stop the infection.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed