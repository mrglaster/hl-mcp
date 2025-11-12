# register_library
#### Syntax
```
native register_library(const library[]);
```

#### Description
```
Registers the plugin as a library.
```

#### Note
```
To mark a library as required, place the following in the include
file:
#pragma reqlib <name>
#if !defined AMXMODX_NOAUTOLOAD
   #pragma loadlib <name>
#endif
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

