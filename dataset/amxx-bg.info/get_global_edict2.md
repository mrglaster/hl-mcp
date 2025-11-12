# get_global_edict2
#### Syntax
```
native get_global_edict2(variable);
```

#### Usage
variable | ```Entry to retrieve from```
---|---
#### Description
```
Returns a edict type value from the server globals.
```

#### Note
```
For a list of valid edict type entries, see the GL_* constants in
engine_const.inc under the "Edict" section.
```

#### Note
```
This native returns -1 as a safe error value if the edict retrieved is
an invalid entity. Otherwise it is identical to get_global_edict().
```

#### Return
```
Value of specified entry
```

#### Error
```
If an invalid entry is provided, an error will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

