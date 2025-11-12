# get_modname
#### Syntax
```
native get_modname(name[], len);
```

#### Usage
name | ```Buffer to copy mod name to```
---|---
len | ```Maximum size of the buffer```
#### Description
```
Retrieves the name of the currently played mod.
```

#### Note
```
This retrieves the short name of the mod. Example: for Counter-Strike,
it will copy "cstrike" to the buffer.
```

#### Return
```
Number of cells written to buffer
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

