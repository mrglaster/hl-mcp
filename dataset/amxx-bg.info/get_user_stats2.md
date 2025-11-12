# get_user_stats2
#### Syntax
```
native get_user_stats2(index, stats[STATSX_MAX_OBJECTIVE]);
```

#### Usage
index | ```Client index```
---|---
stats | ```Buffer to copy statistics to```
#### Description
```
Retrieves the client's objective statistics from the permanent storage.
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