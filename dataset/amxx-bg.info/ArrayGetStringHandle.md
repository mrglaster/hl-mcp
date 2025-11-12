# ArrayGetStringHandle
#### Syntax
```
native DoNotUse:ArrayGetStringHandle(Array:which, item);
```

#### Usage
which | ```Array handle```
---|---
item | ```Item to retrieve handle of```
#### Description
```
Creates a special handle that can be passed to a string format routine for
printing as a string (with the %a format option).
```

#### Note
```
It is recommended to pass the function as a parameter to the format
routine directly. The array item must contain a null-terminated string!
```

#### Note
```
Do not save or otherwise use the handles returned by this function.
```

#### Note
```
Example usage:
console_print(id, "%a", ArrayGetStringHandle(MessageArray, i));
```

#### Return
```
Handle to the item
```

#### Error
```
If an invalid handle or an invalid index is provided an
error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

