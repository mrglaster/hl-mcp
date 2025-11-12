# eng_get_string
#### Syntax
```
native eng_get_string(_string, _returnString[], _len);
```

#### Usage
_string | ```String table index```
---|---
_returnString | ```Buffer to copy string to```
_len | ```Maximum size of buffer```
#### Description
```
Retrieves a string from the engine string table.
```

#### Return
```
Number of cells written to buffer
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

