# get_user_stats
#### Syntax
```
native get_user_stats(index, stats[STATSX_MAX_STATS], bodyhits[MAX_BODYHITS]);
```

#### Usage
index | ```Client index```
---|---
stats | ```Buffer to copy statistics to```
bodyhits | ```Buffer to copy body hits to```
#### Description
```
Retrieves the client's weapon statistics from the permanent storage on the
server.
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
Players rank > 0 on success, or 0 if player is not ranked
and no statistics are available
```

#### Error
```
If an invalid client index is provided, an error will be
thrown.
```


This code is a part of csstats.inc. To use this code you should include csstats.inc as ```#include <csstats>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).