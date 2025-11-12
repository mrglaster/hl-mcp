# player_kick_post
#### Syntax
```
forward player_kick_post(id, szPlayerData[PlayerData]);
```

#### Description
```
@description             Multiforward called right before a player will be kicked to free a player slot.

@param id                Choosen player to be kicked index.
@param szPlayerData      Array which contains data of the reserved client.

@return                  Forward ignores return values.
```


This code is a part of advanced_slot_res.inc. To use this code you should include advanced_slot_res.inc as ```#include <advanced_slot_res>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. 