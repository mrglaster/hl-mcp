# get_xvar_float
#### Syntax
```
native Float:get_xvar_float(id);
```

#### Usage
id | ```Xvar id, an xvar id can be retrieved using get_xvar_id()```
---|---
#### Description
```
Returns the float value of a public variable.
```

#### Note
```
If multiple plugins declare the same public variable, they are not
automatically synchronized. The xvar system accesses only one of all
public variables directly. Xvars have to be read through the natives or
the value will be incorrect.
```

#### Return
```
Xvar float value
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

