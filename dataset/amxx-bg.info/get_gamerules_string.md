# get_gamerules_string
#### Syntax
```
native get_gamerules_string(const class[], const member[], value[], maxlen, element = 0);
```

#### Usage
class | ```Class name```
---|---
member | ```Member name```
value | ```Buffer to store data in```
maxlen | ```Maximum size of the buffer```
element | ```Element to retrieve (starting from 0) if member is an array```
#### Description
```
Retrieves a string from the gamerules object based off a class and member name.
```

#### Note
```
This native is used to access the following (C++/engine) data types:
string, stringptr.
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If member is empty, no offset is found or an invalid offset
is retrieved, or the data type does not match, an error will
be thrown.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

