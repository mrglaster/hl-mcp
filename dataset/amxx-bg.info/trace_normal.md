# trace_normal
#### Syntax
```
native trace_normal(iIgnoreEnt, const Float:fStart[3], const Float:fEnd[3], Float:vReturn[3]);
```

#### Usage
iIgnoreEnt | ```Entity index that trace will ignore, -1 if trace should not ignore any entities```
---|---
fStart | ```Trace starting point```
fEnd | ```Trace target point```
vReturn | ```Vector to copy trace normal to```
#### Description
```
Fires a trace line between two origins, retrieving the trace normal.
```

#### Note
```
This native writes to the global engine module trace handle. Additional
trace results can be retrieved using traceresult().
```

#### Return
```
1 if a normal is available (trace hit something), 0
otherwise
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

