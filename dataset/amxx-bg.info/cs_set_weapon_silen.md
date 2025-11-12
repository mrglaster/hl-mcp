# cs_set_weapon_silen
#### Syntax
```
native cs_set_weapon_silen(index, silence = 1, draw_animation = 1);
```

#### Usage
index | ```Weapon entity index```
---|---
silence | ```If nonzero the weapon will be put into silenced mode, otherwise the silenced mode will be removed```
draw_animation | ```If 1 and the weapon is currently held by a client, the appropriate weapon animation will be played If 2, same as 1 but follows game behavior by playing the associated player's model sequence and disallowing firing while animation is playing.```
#### Description
```
Sets the weapon's silenced mode.
```

#### Note
```
Only the USP and M4A1 can be set to silenced fire mode as they are the
only guns in the game that provide such a mode.
```

#### Note
```
This native does not verify that the provided entity is a weapon
entity. It will result in undefined behavior if used on non-weapon
entities.
```

#### Return
```
1 if silenced mode set successfully, 0 if entity is
not an applicable weapon
```

#### Error
```
If an invalid entity index or a client index is
provided, an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).