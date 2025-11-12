# find_gamerules_info
#### Syntax
```
native find_gamerules_info(const class[], const member[], &FieldType:type = FIELD_NONE, &arraysize = 0, &bool:unsigned = false);
```

#### Usage
class | ```Class name```
---|---
member | ```Member name```
type | ```Optional variable to store member type in (FIELD_* constants)```
arraysize | ```Optional variable to store array size in, if member is an array```
unsigned | ```Optional variable to store whether member is unsigned (short and char types only)```
#### Description
```
Finds a gamerules offset based off a class and member name.
```

#### Return
```
Class member offset
```

#### Error
```
If either class or member is empty, no offset is found or an invalid
offset is retrieved, an error will be thrown.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

