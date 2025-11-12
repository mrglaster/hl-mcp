# ArrayFindValue
#### Syntax
```
native ArrayFindValue(Array:which, any:item);
```

#### Usage
which | ```Array handle```
---|---
item | ```Value to search for```
#### Description
```
Searches through the array and returns the index of the first occurence of
the specified value.
```

#### Return
```
Array index on success, -1 if the value can't be found
```

#### Error
```
If an invalid handle is provided an error will be
thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

