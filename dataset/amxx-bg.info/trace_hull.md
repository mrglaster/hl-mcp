# trace_hull
#### Syntax
```
native trace_hull(const Float:origin[3], hull, ignoredent = 0, ignoremonsters = 0, const Float:end[3] = NULL_VECTOR);
```

#### Usage
origin | ```Trace start point (and end point if not specified)```
---|---
hull | ```Hull type```
ignoredent | ```Entity index that trace will ignore```
ignoremonsters | ```Entity ignore type```
end | ```Trace end point, pass NULL_VECTOR to use start point```
#### Description
```
Fires a trace hull on a specified origin or between two origins.
```

#### Note
```
This native writes to the global engine module trace handle. Additional
trace results can be retrieved using traceresult().
```

#### Note
```
For a list of valid hull types see the HULL_* constants in
hlsdk_const.inc
```

#### Note
```
For a list of valid ignore types see the *IGNORE_* constants in
hlsdk_const.inc
```

#### Return
```
Custom bitflag sum of relevant trace results
StartSolid (1), AllSolid (2) and InOpen (4)
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

