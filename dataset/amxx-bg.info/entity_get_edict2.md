# entity_get_edict2
#### Syntax
```
native entity_get_edict2(iIndex, iKey);
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
This native returns -1 as a safe error value if the edict retrieved
from the entvar is an invalid entity. Otherwise it is identical to
entity_get_edict().
```

#### Return
```
Entity index in specified entry, -1 if the edict in the
entvar is not a valid entity or an invalid entry was
specified
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

