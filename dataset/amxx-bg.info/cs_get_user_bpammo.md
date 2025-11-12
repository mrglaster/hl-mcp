# cs_get_user_bpammo
#### Syntax
```
native cs_get_user_bpammo(index, weapon);
```

#### Usage
index | ```Client index```
---|---
weapon | ```Weapon id```
#### Description
```
Returns amount of ammo in the client's backpack for a specific weapon.
```

#### Note
```
For a list of possible weapon ids see the CSW_* constants in
amxconst.inc
```

#### Note
```
Some weapons share ammo types and therefore ammo backpack pools. List
of ammo types:
ammo_338magnum  - awp
ammo_762nato    - scout, ak47, g3sg1
ammo_556natobox - m249
ammo_556nato    - famas, m4a1, aug, sg550, galil, sg552
ammo_buckshot   - m3, xm1014
ammo_45acp      - usp, ump45, mac10
ammo_57mm       - fiveseven, p90
ammo_50ae       - deagle
ammo_357sig     - p228
ammo_9mm        - glock, mp5, tmp, elites
/               - hegrenade
/               - flashbang
/               - smokegrenade
```

#### Return
```
Amount of ammo in backpack
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, the client is not connected, or an invalid
weapon id is provided, an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).