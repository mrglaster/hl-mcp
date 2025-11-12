# ArrayPushArray
#### Syntax
```
native ArrayPushArray(Array:which, const any:input[], size = -1);
```

#### Usage
which | ```Array handle```
---|---
input | ```Array to copy to the cellarray```
size | ```If not set, assumes the buffer size is equal to the cellsize. Otherwise, the specified size is used.```
#### Description
```
Creates a new item at the end of the cellarray and copies the provided array
into it.
```

#### Note
```
The input will be truncated if it is bigger than the cellsize the array
was created with.
```

#### Return
```
Index of the new entry
```

#### Error
```
If an invalid handle is provided or the resizing
operation runs out of memory, an error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

