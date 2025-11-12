# get_tr
#### Syntax
```
native get_tr(TraceResult:tr_member, any:...);
```

#### Description

get_tr - Returns value of tr_member within the trace. 
Only use this with functions that pass a Trace, such as a TraceLine forward registered with FakeMeta.

With no extra parameters this returns an integer value. With one extra parameter this a returns float or vector value by reference. 

This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

