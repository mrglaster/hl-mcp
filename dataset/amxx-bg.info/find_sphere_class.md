# find_sphere_class
#### Syntax
```
native find_sphere_class(aroundent, const _lookforclassname[], Float:radius, entlist[], maxents, const Float:origin[3] = {0.0, 0.0, 0.0});
```

#### Usage
aroundent | ```Entity index to center sphere around, < 1 to use origin```
---|---
_lookforclassname | ```Classname to match```
radius | ```Sphere radius```
entlist | ```Array to store entities in```
maxents | ```Maximum size of array```
origin | ```Center of sphere, used if aroundent < 1```
#### Description
```
Searches for entities inside a sphere around a specified entity or origin,
matching by classname.
```

#### Note
```
This native always starts searching from entity index 0, there is no
way to specify the starting point. If the entlist array is not big
enough to accomodate all entities, the results will be truncated.
```

#### Return
```
Number of entities stored in entlist
```

#### Error
```
If an invalid entity index is provided or, if
the index is a client index, the client is not
connected, an error will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

