# client_damage
#### Syntax
```
forward client_damage(attacker, victim, damage, wpnindex, hitplace, TA);
```

#### Usage
attacker | ```Attacker client index```
---|---
victim | ```Victim client index```
damage | ```Damage dealt to victim```
wpnindex | ```Weapon id```
hitplace | ```Body hitplace```
ta | ```If nonzero the attack was a team attack```
#### Description
```
Called after a client attacks another client.
```

#### Note
```
For a list of possible weapon ids see the CSW_* constants in
amxconst.inc
```

#### Note
```
For a list of possible body hitplaces see the HIT_* constants in
amxconst.inc
```

#### Return
```
This forward ignores the return value.
```


This code is a part of csx.inc. To use this code you should include csx.inc as ```#include <csx>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).