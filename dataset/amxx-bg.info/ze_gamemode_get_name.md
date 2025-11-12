# ze_gamemode_get_name
#### Syntax
```
native ze_gamemode_get_name(const game_id, szName[], iLen);
```

#### Usage
szName[] | ```The buffer to store string in.```
---|---
iLen | ```Character size of the output buffer.```
#### Description
```
Description:     Gets a game mode's name.
```

#### Return
```
true  | If successfully.
false | Otherwise.
```

#### Error
```
If a game mode ID is invalid.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed