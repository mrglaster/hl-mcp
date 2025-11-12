# get_string
#### Syntax
```
native get_string(param, dest[], maxlen);
```

#### Usage
param | ```Argument to retrieve, starting from 1```
---|---
dest | ```Buffer to copy string to```
maxlen | ```Maximum size of buffer```
#### Description
```
Retrieves a string from the plugin calling the native.
```

#### Return
```
Number of cells copied to buffer
```

#### Error
```
If used outside of a native callback, or the native was
created with style 1, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

