# cs_create_entity
#### Syntax
```
native cs_create_entity(const classname[]);
```

#### Usage
classname | ```Entity class name```
---|---
#### Description
```
Creates an entity using Counter-Strike's custom CreateNamedEntity wrapper.
```

#### Note
```
Unlike other mods CS keeps track of entities using a custom hashtable.
This function adds entities to this hashtable, providing benefits over
the default CreateNamedEntity (used by create_entity() for example):
- Storing entities in a hashtable allows CS to improve classname lookup
  performance compared to functions like FindEntityByString (used by
  find_ent_by_class() for example) that usually have to loop
  through all entities incrementally.
- As CS exclusively uses the hashtable for classname lookup, entities
  created using the default engine functions will not be found by the
  game. For example "weaponbox" entities are supposed to be
  automatically cleaned up on round restart but are not considered if
  they have not been added to the hashtable.
```

#### Note
```
The faster hashtable lookup can be utilized with cs_find_ent_by_class()
```

#### Note
```
When creating an entity the classname has to be valid in the mod, as
the engine needs to link the entity to an existing class internally.
The classname string that is stored in the entvar struct
(EV_SZ_classname) is separate from this association and can later be
freely changed to serve other purposes.
```

#### Return
```
Index of the created entity (> 0), 0 otherwise
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).