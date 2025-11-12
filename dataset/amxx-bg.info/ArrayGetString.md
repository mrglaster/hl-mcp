# ArrayGetString
#### Syntax
```
native ArrayGetString(Array:which, item, output[], size);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item index in the array```
output | ```Buffer to copy value to```
size | ```Maximum size of the buffer```
#### Description
```
Returieves string data from an array.
```

#### Return
```
Number of characters copied
```

#### Error
```
If an invalid handle or an invalid index is provided an
error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

