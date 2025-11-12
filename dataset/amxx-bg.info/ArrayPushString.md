# ArrayPushString
#### Syntax
```
native ArrayPushString(Array:which, const input[]);
```

#### Usage
which | ```Array handle```
---|---
input | ```String to copy to the array```
#### Description
```
Creates a new item at the end of the array and copies the provided string
into it.
```

#### Note
```
The input will be truncated if it is longer than the cellsize the array
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


  
  

