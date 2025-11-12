# get_gamerules_entity
#### Syntax
```
native get_gamerules_entity(const class[], const member[], element = 0);
```

#### Usage
class | ```Class name```
---|---
member | ```Member name```
element | ```Element to retrieve (starting from 0) if member is an array```
#### Description
```
Retrieves an entity index from the gamerules object based off a class
and member name.
```

#### Note
```
This native is used to access the following (C++/engine) data types:
classptr, entvars, edict and ehandle.
```

#### Return
```
Entity index if found, -1 otherwise
```

#### Error
```
If member is empty, no offset is found or an invalid offset
is retrieved, or the data type does not match, an error will
be thrown.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

