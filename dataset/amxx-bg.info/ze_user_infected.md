# ze_user_infected
#### Syntax
```
forward ze_user_infected(iVictim, iInfector);
```

#### Usage
iVictim | ```Victim index, human who catch the infection.```
---|---
iInfector | ```Infector index, zombie or server who caused the infection.```
#### Description
```
Description:     Called when user infected by player or by the server.
                 Called also at the first choose of zombies (in this case server is the infector).
```

#### Return
```
This forward ignores the return value.
```

#### Note
```
If the infector is the server, The iInfector will be 0
else the iInfector will be the zombie id.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed