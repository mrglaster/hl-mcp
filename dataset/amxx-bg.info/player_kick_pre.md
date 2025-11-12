# player_kick_pre
#### Syntax
```
forward player_kick_pre(id, szPlayerData[PlayerData]);
```

#### Description
```
@description             Multiforward called before a player will be kicked to free a player slot.

@param id                Choosen player to be kicked index.
@param szPlayerData      Array which contains data of the reserved client.

@return                  Return SLOT_KICK_YES if you want to not let the plugin kick the player or SLOT_KICK_NO to continue executing.
```


This code is a part of advanced_slot_res.inc. To use this code you should include advanced_slot_res.inc as ```#include <advanced_slot_res>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. 