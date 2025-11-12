# global_get
#### Syntax
```
native global_get(_value, any:...);
```

#### Description
```
Returns any global variable inside globalvars_t structure. Use the glb_* enum.

When returning data from glb_pStringBase (the global string table), you may give a pointer into that table
in order to get different strings.
Example:
new model[128]
new ptr = pev(id, pev_viewmodel)
global_get(glb_pStringBase, ptr, model, 127)
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

