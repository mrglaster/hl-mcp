# ze_gamemode_register
#### Syntax
```
native ze_gamemode_register(const szName[]);
```

#### Usage
szName[] | ```Game mode name.```
---|---
#### Description
```
Description:     Registers a new game mode.
```

#### Return
```
A game mode ID, or ZE_WRONG_GAME on failure.
```

#### Note
```
Max length of game mode name is 32 characters.
```

#### Error
```
If game mode name is already exists, or game mode without name.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed