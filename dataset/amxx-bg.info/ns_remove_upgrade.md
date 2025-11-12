# ns_remove_upgrade
#### Syntax
```
native ns_remove_upgrade(idPlayer, upgrade);
```

#### Description
```
Removes an upgrade from the player's bought and active upgrade lists.
This will not refund the points spent on the upgrade, nor will it
immediately strip the upgrade if the player is alive.  Rather, it will
make it so the player no longer receives the upgrade on spawn.
```

#### Note
```
This only works in combat.
```

#### Params
```
idPlayer     The player index to change upgrades for.
```

#### Params
```
ugprade      The impulse number for the upgrade to strip.
```

#### Return
```
2 for upgrade removed from player's bought and active list.
1 for upgrade removed from player's bought list only.
3 for upgrade removed from player's active list only (shouldn't happen, just incase.)
0 for the player didn't have the upgrade in either list.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).