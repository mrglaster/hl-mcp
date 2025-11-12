# ze_player_disconnect
#### Syntax
```
forward ze_player_disconnect(id);
```

#### Usage
id | ```Client index.```
---|---
#### Description
```
Description:          Called when player disconnect.
```

#### Return
```
ZE_CONTINUE | Continue Mod game rules.
ZE_STOP     | Block Mod game rules, you can use yours.
```

#### Note
```
Useful in plugins like, replacing disconnected zombie/human if he was last zombie/human.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed