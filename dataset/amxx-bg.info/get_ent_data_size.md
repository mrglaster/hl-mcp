# get_ent_data_size
#### Syntax
```
native get_ent_data_size(const class[], const member[]);
```

#### Usage
class | ```Class name```
---|---
member | ```Member name```
#### Description
```
Retrieves the size of array of n entity class member.
```

#### Return
```
Size of array (in elements), otherwise 1 if member is not an array
```

#### Error
```
If either class or member is empty, no offset is found or an invalid
offset is retrieved, an error will be thrown.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

