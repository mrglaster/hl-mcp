# set_gamerules_entity
#### Syntax
```
native set_gamerules_entity(const class[], const member[], value, element = 0);
```

#### Usage
class | ```Class name```
---|---
member | ```Member name```
value | ```Entity index to set```
element | ```Element to set (starting from 0) if member is an array```
#### Description
```
Sets an entity index to the gamerules object based off a class
and member name.
```

#### Note
```
This native is used to access the following (C++/engine) data types:
classptr, entvars, edict and ehandle.
```

#### Note
```
Pass -1 as value to act as C++ NULL.
```

#### Return
```
This function has no return value.
```

#### Error
```
If member is empty, no offset is found or an invalid offset
is retrieved, or the data type does not match, an error will
be thrown.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

