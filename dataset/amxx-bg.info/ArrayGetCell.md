# ArrayGetCell
#### Syntax
```
native any:ArrayGetCell(Array:which, item, block = 0, bool:asChar = false);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item index in the array```
block | ```If the array has a cellsize >1 this optionally specifies which block to read from```
asChar | ```If true reads the value as a byte instead of a cell```
#### Description
```
Returns a single cell of data from an array
```

#### Return
```
Integer value
```

#### Error
```
If an invalid handle, index or block is provided an
error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

