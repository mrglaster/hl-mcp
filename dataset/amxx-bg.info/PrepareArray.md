# PrepareArray
#### Syntax
```
native PrepareArray(const array[], size, copyback = 0);
```

#### Usage
array | ```Array to prepare```
---|---
size | ```Size of array```
copyback | ```If nonzero, modifications made by the called plugin(s) will be copied back to the caller```
#### Description
```
Prepares an array for use in a forward. Pass the result ExecuteForward()
instead of the array itself.
```

#### Return
```
Special handle for use in ExecuteForward()
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

