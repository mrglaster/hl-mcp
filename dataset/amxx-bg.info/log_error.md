# log_error
#### Syntax
```
native log_error(error, const fmt[], any:...);
```

#### Usage
error | ```Error number```
---|---
fmt | ```Formatting rules```
... | ```Variable number of formatting parameters```
#### Description
```
Logs an error in the native and breaks into the AMXX debugger.
```

#### Note
```
This acts as if the calling plugin - the plugin that is calling the
native, not the plugin calling this function - triggered the error,
just like when AMXX natives error.
```

#### Return
```
This function has no return value.
```

#### Error
```
The function is guaranteed to throw an error, but will make
it appear as if the plugin calling the native triggered it.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

