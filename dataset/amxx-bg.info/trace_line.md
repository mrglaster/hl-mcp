# trace_line
#### Syntax
```
native trace_line(iIgnoreEnt, const Float:fStart[3], const Float:fEnd[3], Float:vReturn[3]);
```

#### Usage
iIgnoreEnt | ```Entity index that trace will ignore, -1 if trace should not ignore any entities```
---|---
fStart | ```Trace starting point```
fEnd | ```Trace target point```
vReturn | ```Vector to copy trace end point to```
#### Description
```
Fires a trace line between two origins, retrieving the end point and entity
hit.
```

#### Note
```
This native writes to the global engine module trace handle. Additional
trace results can be retrieved using traceresult().
```

#### Note
```
This native returns 0 if the trace did not hit anything. As 0 is an
entity index that is considered to be a valid value for a trace hit
("worldspawn"), this native can potentially return a misleading value.
Check other components of the trace result to verify the entity index.
```

#### Return
```
Entity index if trace hit an entity, 0 otherwise
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

