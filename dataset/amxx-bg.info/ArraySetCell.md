# ArraySetCell
#### Syntax
```
native ArraySetCell(Array:which, item, any:input, block = 0, bool:asChar = false);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item index in the array```
input | ```Value to set```
block | ```If the array has a cellsize >1 this optionally specifies which block to write to```
asChar | ```If true writes the value as a byte instead of a cell```
#### Description
```
Sets an item's data to a single cell value.
```

#### Note
```
The item index must already be valid. Use ArrayPushArray to create
a new array item in the cellarray.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid handle, index or block is provided an
error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

