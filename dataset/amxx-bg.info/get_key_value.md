# get_key_value
#### Syntax
```
native get_key_value(const pbuffer, const key[], const value[], const maxlen);
```

#### Usage
pbuffer | ```Pointer to buffer```
---|---
key | ```Key string```
value | ```Buffer to copy value to```
maxlen | ```Maximum size of the buffer```
#### Description
```
Gets value for key in buffer
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If invalid buffer handler provided, an error will be thrown.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.