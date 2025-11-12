# get_stats
#### Syntax
```
native get_stats(index, stats[STATSX_MAX_STATS], bodyhits[MAX_BODYHITS], name[], len, authid[] = "", authidlen = 0);
```

#### Usage
index | ```Rank index```
---|---
stats | ```Buffer to copy statistics to```
bodyhits | ```Buffer to copy body hits to```
name | ```Buffer to copy client name to```
len | ```Maximum name buffer size```
authid | ```Buffer to copy client auth id to```
authidlen | ```Maximum authid buffer size```
#### Description
```
Retrieves statistics from the permanent storage on the server via iterative,
incremental access.
```

#### Note
```
The permanent storage is updated on every respawn or client disconnect.
```

#### Note
```
Player rank is determined by the customizable "get_score" function in
"data/csstats.amxx". By default it uses the difference of kills to
deaths/teamkills.
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
   7 - Rank
```

#### Return
```
Next rank index (> 0 and > index), or 0 if no more
statistics exist
```


This code is a part of csstats.inc. To use this code you should include csstats.inc as ```#include <csstats>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).