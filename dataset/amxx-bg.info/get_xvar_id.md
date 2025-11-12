# get_xvar_id
#### Syntax
```
native get_xvar_id(const name[]);
```

#### Usage
name | ```Variable name```
---|---
#### Description
```
Returns a unique id for a public variable.
```

#### Note
```
Variables declared with the "public" specifier are accessible by-name
from outside of the declaring plugin.
```

#### Note
```
If multiple plugins declare the same public variable, this native will
still return a unique id.
```

#### Return
```
Xvar id on success, -1 on failure
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

