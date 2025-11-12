# trace_forward
#### Syntax
```
native trace_forward(const Float:start[3], const Float:angle[3], Float:give, ignoreEnt, &Float:hitX, &Float:hitY, &Float:shortestDistance, &Float:shortestDistLow, &Float:shortestDistHigh);
```

#### Usage
start | ```Starting origin```
---|---
angle | ```Trace line direction```
give | ```Units that a trace line can be longer than the shortest trace line to still be considered hitting the same obstacle```
ignoreEnt | ```Entity index that traces will ignore, -1 if traces should not ignore any entities```
hitX | ```Variable to store X axis value of shortest trace line endpoint in```
hitY | ```Variable to store Y axis value of shortest trace line endpoint in```
shortestDistance | ```Variable to store length of shortest trace line in```
shortestDistLow | ```Variable to store Z axis offset of shortest trace line in```
shortestDistHigh | ```Variable to store Z axis offset of highest trace line that satisfies "give" condition in```
#### Description
```
Attempts to describe an obstacle by firing trace lines in a specified
direction, offset on the z-axis around an origin.
```

#### Note
```
The functionality of this native can mostly be replaced by a single
hull trace. This native does not write to the global engine module
trace handle.
```

#### Note
```
This native is intended to examine an obstacle in front of a standing
player. Start should usually be the origin of a client while angle
should be its forward angle vector. 73 traces are fired, each offset by
one unit on the z-axis from the last, starting at -36 and moving up to
+36. This is because a standing player model is 72 units high, so 73
units of clearance are required to fit them. The values stored in the
various parameters then attempt to describe the obstacle.
```

#### Note
```
To fully understand the nuances of the algorithm it is necessary to
view its source code located in engine.cpp of the engine module.
```

#### Return
```
This function has no return value.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

