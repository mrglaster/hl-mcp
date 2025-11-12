# set_xvar_num
#### Syntax
```
native set_xvar_num(id, value = 0);
```

#### Usage
id | ```Xvar id, an xvar id can be retrieved using get_xvar_id()```
---|---
value | ```Value to set```
#### Description
```
Sets the integer value of a public variable.
```

#### Note
```
If multiple plugins declare the same public variable, they are not
automatically synchronized. The xvar system accesses only one of all
public variables directly. Xvars have to be set through the natives or
the xvar will not be updated.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid xvar id is specified, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

