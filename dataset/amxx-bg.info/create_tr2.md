# create_tr2
#### Syntax
```
native create_tr2();
```

#### Description
```
Creates a traceresult handle.  This value should never be altered.
The handle can be used in get/set_tr2 and various traceresult engine functions.

NOTE: You must call free_tr2() on every handle made with create_tr2().
```

#### Return
```
A new TraceResult handle.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

