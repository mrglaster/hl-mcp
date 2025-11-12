# ArraySetArray
#### Syntax
```
native ArraySetArray(Array:which, item, const any:input[], size =-1);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item index in the array```
input | ```Array to copy to the cellarray```
size | ```If not set, assumes the buffer size is equal to the cellsize. Otherwise, the specified size is used.```
#### Description
```
Fills an item's data with the contents of an array.
```

#### Note
```
If the size parameter is specified as -1 the input buffer has to match
the size the array was created with.
```

#### Note
```
The item index must already be valid. Use ArrayPushArray to create
a new array item in the cellarray.
```

#### Return
```
Number of cells copied
```

#### Error
```
If an invalid handle or an invalid index is provided an
error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

