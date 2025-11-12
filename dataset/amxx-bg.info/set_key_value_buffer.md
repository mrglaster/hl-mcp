# set_key_value_buffer
#### Syntax
```
native set_key_value_buffer(const pbuffer, const value[], const maxlen = -1);
```

#### Usage
buffer | ```Pointer to buffer```
---|---
value | ```Value to set```
maxlen | ```Maximum size of the value buffer to set, -1 means copy all characters```
#### Description
```
Sets value string to entire buffer
```

#### Return
```
1 on success, 0 otherwise
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.