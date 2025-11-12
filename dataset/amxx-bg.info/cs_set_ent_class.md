# cs_set_ent_class
#### Syntax
```
native cs_set_ent_class(index, const classname[]);
```

#### Usage
index | ```Entity index```
---|---
classname | ```Classname to update for```
#### Description
```
Sets a custom classname of an entity.
```

#### Note
```
Unlike other mods CS keeps track of entities using a custom hashtable.
This function adds or updates the classname in the hasthable as well.
This is useful for use with cs_find_ent_by_class() and cs_find_ent_by_owner().
```

#### Return
```
This function has no return value.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).