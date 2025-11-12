# ArrayInsertStringBefore
#### Syntax
```
native ArrayInsertStringBefore(Array:which, item, const input[]);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item index in the array```
input | ```String to copy to the array```
#### Description
```
Creates a new item in front of the specified item and copies the provided
string into it. All items beyond it get shifted up by one.
```

#### Note
```
The input will be truncated if it is longer than the cellsize the array
was created with.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid handle or an invalid index is provided an
error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

