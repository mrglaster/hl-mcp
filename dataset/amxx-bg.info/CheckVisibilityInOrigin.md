# CheckVisibilityInOrigin
#### Syntax
```
native CheckVisibilityInOrigin(const ent, Float:origin[3], CheckVisibilityType:type = VisibilityInPVS);
```

#### Usage
entity | ```Entity index```
---|---
origin | ```Vector representing the origin from which visibility is checked```
type | ```Type of visibility check: VisibilityInPVS (Potentially Visible Set) or VisibilityInPAS (Potentially Audible Set)```
#### Description
```
Test visibility of an entity from a given origin using either PVS or PAS
```

#### Return
```
0 - Not visible
1 - Visible, passed by a leafnum
2 - Visible, passed by a headnode
```

#### Remarks
```
This function checks the visibility of the specified entity from the given origin, using either
the Potentially Visible Set (PVS) or the Potentially Audible Set (PAS) depending on the provided type
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.