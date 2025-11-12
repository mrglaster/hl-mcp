# ArrayResize
#### Syntax
```
native bool:ArrayResize(Array:which, newsize);
```

#### Usage
which | ```Array handle```
---|---
newsize | ```New size```
#### Description
```
Resizes an array.
```

#### Note
```
If the size is smaller than the current array size the array is
truncated and data lost.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid handle is provided or the resizing
operation runs out of memory, an error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

