# set_pev_string
#### Syntax
```
native set_pev_string(_index, _value, _string);
```

#### Usage
_index | ```The entity index to set the value on.```
---|---
_value | ```The pev field to set - MUST be a string field.```
_string | ```The string handle, retrieved from places like AllocString.```
#### Description
```
Use this native to set a pev field to a string that is already allocated (via a function such
as EngFunc_AllocString).
```

#### Note
```
If you specify _value as anything other than string fields, an error will be thrown.
```

#### Note
```
Pass 0 as the _string field to set it to an empty string.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

