# create_entity
#### Syntax
```
native create_entity(const szClassname[]);
```

#### Usage
szClassname | ```Entity classname```
---|---
#### Description
```
Creates an entity.
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
Entity index > 0 on success, 0 otherwise
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

