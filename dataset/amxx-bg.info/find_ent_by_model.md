# find_ent_by_model
#### Syntax
```
native find_ent_by_model(iIndex, const szClass[], const szModel[]);
```

#### Usage
iIndex | ```Entity index to start from```
---|---
szClass | ```Classname to match```
szModel | ```Model to match```
#### Description
```
Searches entities in the world, starting at a specified index and matching by
classname and model.
```

#### Return
```
Entity index if an entity was found, 0 otherwise
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

