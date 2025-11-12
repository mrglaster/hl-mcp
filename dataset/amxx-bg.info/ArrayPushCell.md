# ArrayPushCell
#### Syntax
```
native ArrayPushCell(Array:which, any:input);
```

#### Usage
which | ```Array handle```
---|---
input | ```Value to set```
#### Description
```
Creates a new item at the end of the array and sets the item's single cell
value.
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


  
  

