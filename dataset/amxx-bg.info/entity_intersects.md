# entity_intersects
#### Syntax
```
native bool:entity_intersects(entity, other);
```

#### Usage
entity | ```Entity index 1```
---|---
other | ```Entity index 2```
#### Description
```
Returns if two entities bounding boxes intersect by comparing their absolute
minimum and maximum origins.
```

#### Return
```
True if entities intersect, false otherwise
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

