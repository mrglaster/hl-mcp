# callfunc_push_array
#### Syntax
```
native callfunc_push_array(const VALUE[], array_size, bool:copyback = true);
```

#### Usage
VALUE | ```Array to push```
---|---
array_size | ```Size of the array```
copyback | ```If true, any changes made in the called function will be copied back to the calling plugin```
#### Description
```
Pushes an array onto the current call.
```

#### Note
```
This will defy the "const" specifier if copyback is true, which is
only kept for special backwards compatibility.
```

#### Return
```
This function has no return value.
```

#### Error
```
If called without initiating a callfunc, or the maximum
amount of parameters is reached, an error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

