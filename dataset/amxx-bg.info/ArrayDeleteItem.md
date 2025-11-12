# ArrayDeleteItem
#### Syntax
```
native ArrayDeleteItem(Array:which, item);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item to delete```
#### Description
```
Deletes an item from the array. All items beyond it get shifted down by one.
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


  
  

