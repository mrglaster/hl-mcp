# set_gamerules_int
#### Syntax
```
native set_gamerules_int(const class[], const member[], any:value, element = 0);
```

#### Usage
class | ```Class name```
---|---
member | ```Member name```
value | ```Value to set```
element | ```Element to set (starting from 0) if member is an array```
#### Description
```
Sets an integer value to the gamerules objecta based off a class
and member name.
```

#### Note
```
This native is used to access the following (C++/engine) data types:
integer, boolean, short, character, pointer, stringint and function.
Unsigned variants (if applicable) are supported and will be converted
automatically.
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


  
  

