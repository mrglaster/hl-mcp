# cs_find_ent_by_class
#### Syntax
```
native cs_find_ent_by_class(start_index, const classname[]);
```

#### Usage
start_index | ```Entity index to start searching from. -1 to start from the first entity```
---|---
classname | ```Classname to search for```
#### Description
```
Finds an entity in the world using Counter-Strike's custom FindEntityByString
wrapper.
```

#### Note
```
Unlike other mods CS keeps track of entities using a custom hashtable.
This function utilizes the hasthable and allows for considerably faster
classname lookup compared to the default FindEntityByString (used by
find_ent_by_class() for example).
```

#### Note
```
This exclusively considers entities in the hashtable, created by the
game itself, using cs_create_entity(), or added via cs_set_ent_class().
```

#### Return
```
Entity index > 0 if found, 0 otherwise
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).