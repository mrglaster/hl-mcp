# ArrayInsertCellBefore
#### Syntax
```
native ArrayInsertCellBefore(Array:which, item, const any:input);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item index in the array```
input | ```Value to set```
#### Description
```
Creates a new item in front of the specified item and sets the item's single
cell value. All items beyond it get shifted up by one.
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


  
  

