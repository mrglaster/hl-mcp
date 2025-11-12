# client_death
#### Syntax
```
forward client_death(killer, victim, wpnindex, hitplace, TK);
```

#### Usage
attacker | ```Attacker client index```
---|---
victim | ```Victim client index```
wpnindex | ```Weapon id```
hitplace | ```Body hitplace```
tk | ```If nonzero the death was a teamkill```
#### Description
```
Called after a client death.
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