# custom_weapon_dmg
#### Syntax
```
native custom_weapon_dmg(weapon, att, vic, damage, hitplace = 0);
```

#### Usage
weapon | ```Custom weapon id```
---|---
att | ```Attacker client index```
vic | ```Victim client index```
damage | ```Damage dealt```
hitplace | ```Optional body hitplace```
#### Description
```
Triggers a damage event on a custom weapon, adding it to the internal stats.
```

#### Note
```
This will also call the client_damage() and client_kill() forwards if
applicable.
```

#### Note
```
For a list of possible body hitplaces see the HIT_* constants in
amxconst.inc
```

#### Return
```
This function has no return value.
```

#### Error
```
If the weapon id is not a custom weapon, an invalid client
index, damage value or hitplace is provided, an error will
be thrown.
```


This code is a part of csx.inc. To use this code you should include csx.inc as ```#include <csx>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).