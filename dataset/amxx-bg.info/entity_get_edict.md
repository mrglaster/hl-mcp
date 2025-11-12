# entity_get_edict
#### Syntax
```
native entity_get_edict(iIndex, iKey);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to retrieve from```
#### Description
```
Returns an edict type value from an entities entvar struct.
```

#### Note
```
For a list of valid edict type entries, see the EV_ENT_* constants in
engine_const.inc
```

#### Note
```
This native returns 0 as an error value if the edict retrieved from the
entvar is an invalid entity. As 0 is an entity index that is
considered to be a valid value for some entvars ("worldspawn"), this
native can potentially return a misleading value. Use
entity_get_edict2() for a safe version.
```

#### Return
```
Entity index in specified entry, 0 if the edict in the
entvar is not a valid entity or an invalid entry was
specified
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

