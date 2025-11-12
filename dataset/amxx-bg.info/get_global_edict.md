# get_global_edict
#### Syntax
```
native get_global_edict(variable);
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
This native returns 0 as an error value if the edict retrieved is an
invalid entity. As 0 is an entity index that is considered to be a
valid value for some globals ("worldspawn"), this native can
potentially return a misleading value. Use get_global_edict2() for a
safe version.
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


  
  

