# get_user_rstats
#### Syntax
```
native get_user_rstats(index, stats[STATSX_MAX_STATS], bodyhits[MAX_BODYHITS]);
```

#### Usage
index | ```Client index```
---|---
stats | ```Buffer to copy statistics to```
bodyhits | ```Buffer to copy body hits to```
#### Description
```
Retrieves the client's statistics from the current round.
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
1 on success, 0 if no statistics are available
```

#### Error
```
If an invalid client index is provided, an error will be
thrown.
```


This code is a part of csstats.inc. To use this code you should include csstats.inc as ```#include <csstats>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).