# force_unmodified
#### Syntax
```
native force_unmodified(force_type, const mins[3], const maxs[3], const filename[]);
```

#### Usage
force_type | ```Enforcement type```
---|---
mins | ```Bounding box mins vector```
maxs | ```Bounding box maxs vector```
filename | ```Filename```
#### Description
```
Forces the clients and server to be running with the same version of a
specified file.
```

#### Note
```
For a list of possible enforcement types, see the force_* constants
in amxconst.inc
```

#### Return
```
1 on success, 0 otherwise
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

