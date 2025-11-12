# is_in_viewcone
#### Syntax
```
native is_in_viewcone(entity, const Float:origin[3], use3d = 0);
```

#### Usage
entity | ```Entity index```
---|---
origin | ```Origin```
use3d | ```If zero the calculation will ignore the z axis (height), if nonzero it is done in 3D```
#### Description
```
Returns if an origin is in an entities view cone. Derived from SDK.
```

#### Note
```
This uses the entities EV_FL_fov value in the calculations and applies
it on all axes. It might be unreliable depending on the use-case.
```

#### Return
```
1 if origin is in view code, 0 otherwise
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

