# ze_gamemode_chosen_pre
#### Syntax
```
forward ze_gamemode_chosen_pre(game_id, bSkipCheck);
```

#### Usage
game_id | ```game mode id.```
---|---
bSkipCheck | ```True when game mode is started by a native.```
#### Description
```
Description:         Called before game mode chosen.
```

#### Return
```
ZE_STOP     | Prevent choosing a game mode.
ZE_CONTINUE | Continue choosing a game mode.
```

#### Note
```
If a game mode is not chosen,
the default game mode will be chosen.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed