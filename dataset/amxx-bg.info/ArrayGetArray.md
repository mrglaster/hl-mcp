# ArrayGetArray
#### Syntax
```
native ArrayGetArray(Array:which, item, any:output[], size = -1);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item index in the array```
output | ```Buffer to copy value to```
size | ```If not set, assumes the buffer size is equal to the cellsize. Otherwise, the specified size is used.```
#### Description
```
Retrieves an array of data from a cellarray.
```

#### Note
```
If the size parameter is specified as -1 the output buffer has to match
the size the array was created with.
```

#### Return
```
Number of cells copied
```

#### Error
```
If an invalid handle or index is provided an error will
be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

