# ArrayCreate
#### Syntax
```
native Array:ArrayCreate(cellsize = 1, reserved = 32);
```

#### Usage
cellsize | ```Size of each array entry in cells```
---|---
reserved | ```Pre-allocates space in the array for the specified number of items. The items are not valid to read or set until they have actually been pushed into the array.```
#### Description
```
Creates a handle to a dynamically sized array.
```

#### Note
```
It is very important that the provided cellsize matches up with the
buffer sizes that are passed with subsequent Array[Get|Set|Push] calls.
```

#### Note
```
Initially the "reserved" parameter was intended to create blank entries
that would immediately be usable with Array[Get|Set] functions. This
functionality was never working as intended, and can now be achieved
using ArrayResize().
```

#### Return
```
New array handle, which must be freed via ArrayDestroy()
```

#### Error
```
If an invalid cellsize is provided an error will be
thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

