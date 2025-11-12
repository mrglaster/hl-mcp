# get_user_vstats
#### Syntax
```
native get_user_vstats(index, victim, stats[STATSX_MAX_STATS], bodyhits[MAX_BODYHITS], wpnname[] = "", len = 0);
```

#### Usage
index | ```Client index```
---|---
victim | ```Victim client index, or 0 to retrieve the statistics against all victims```
stats | ```Buffer to copy statistics to```
bodyhits | ```Buffer to copy body hits to```
wpnname | ```Optional buffer to copy last used weapon name to```
len | ```Maximum buffer size```
#### Description
```
Retrieves the client's statistics inflicted upon another client from the
current round.
```

#### Note
```
For a list of possible body hitplaces see the HIT_* constants in
amxconst.inc
```

#### Note
```
For a list of possible stat constants see the STATSX_* constants in
amxconst.inc
```

#### Note
```
The fields in the statistics are:
   0 - Kills
   1 - Deaths
   2 - Headshots
   3 - Teamkills
   4 - Shots
   5 - Hits
   6 - Damage
```

#### Return
```
1 on success, 0 if no statistics are available against the
specified victim
```

#### Error
```
If an invalid client index is provided, an error will be
thrown.
```


This code is a part of csstats.inc. To use this code you should include csstats.inc as ```#include <csstats>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).