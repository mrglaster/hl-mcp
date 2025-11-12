# get_gamerules_vector
#### Syntax
```
native get_gamerules_vector(const class[], const member[], Float:value[3], element = 0);
```

#### Usage
class | ```Class name```
---|---
member | ```Member name```
value | ```Vector buffer to store data in```
element | ```Element to retrieve (starting from 0) if member is an array```
#### Description
```
Retrieves a vector from the gamerules object based off a class and member name.
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


  
  

