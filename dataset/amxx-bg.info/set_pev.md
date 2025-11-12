# set_pev
#### Syntax
```
native set_pev(_index,_value,any:...);
```

#### Usage
_index | ```The entity index to set the value on.```
---|---
_value | ```The pev field to set, (look in fakemeta_const.inc)```
#### Description
```
Sets entvar data for an entity.  Use the pev_* enum from fakemeta_const.inc for reference.
```

#### Note
```
Setting string data will automatically allocate a new string (via AllocString)
If you have a string already allocated with your own call to AllocString, use
set_pev_string_ptr instead.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

