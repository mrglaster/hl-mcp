# get_stats2
#### Syntax
```
native get_stats2(index, stats[STATSX_MAX_OBJECTIVE], authid[] = "", authidlen = 0);
```

#### Usage
index | ```Client index```
---|---
stats | ```Buffer to copy statistics to```
authid | ```Buffer to copy client auth id to```
authidlen | ```Maximum authid buffer size```
#### Description
```
Retrieves objective statistics from the permanent storage on the server via
iterative, incremental access.
```

#### Note
```
The permanent storage is updated on every respawn or client disconnect.
```

#### Note
```
For a list of possible stat constants see the STATSX_* constants in
amxconst.inc
```

#### Note
```
The fields in the statistics are:
   0 - total defusions
   1 - bomb defused
   2 - bomb plants
   3 - bomb explosions
```

#### Return
```
Next rank index (> 0 and > index), or 0 if no more
statistics exist
```


This code is a part of csstats.inc. To use this code you should include csstats.inc as ```#include <csstats>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).