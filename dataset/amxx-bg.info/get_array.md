# get_array
#### Syntax
```
native get_array(param, dest[], size);
```

#### Usage
param | ```Argument to retrieve, starting from 1```
---|---
dest | ```Buffer to copy array to```
maxlen | ```Size of buffer```
#### Description
```
Retrieves an array from the plugin calling the native.
```

#### Return
```
This function has no return value.
```

#### Error
```
If used outside of a native callback, or the native was
created with style 1, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

