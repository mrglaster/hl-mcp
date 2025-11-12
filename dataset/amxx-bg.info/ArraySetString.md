# ArraySetString
#### Syntax
```
native ArraySetString(Array:which, item, const input[]);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item index in the array```
input | ```String to copy to the array```
#### Description
```
Sets an item's data to a string value.
```

#### Note
```
The input will be truncated if it is longer than the cellsize the array
was created with.
```

#### Note
```
The item index must already be valid. Use ArrayPushString to create
a new array item in the cellarray.
```

#### Return
```
Number of characters copied
```

#### Error
```
If an invalid handle or an invalid index is provided an
error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

