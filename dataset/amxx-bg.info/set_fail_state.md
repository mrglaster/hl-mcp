# set_fail_state
#### Syntax
```
native set_fail_state(const fmt[], any:...);
```

#### Usage
fmt | ```Formatting rules```
---|---
... | ```Variable number of formatting parameters```
#### Description
```
Sets the calling plugin to a failed state.
```

#### Note
```
Calling this will cause the calling plugin to completely cease
operation. It is not possible to recover.
```

#### Note
```
This should be used to gracefully handle fatal errors. The log message
will appear in the AMXX error log.
```

#### Return
```
This function has no return value.
```

#### Error
```
The function is guaranteed to throw a fatal error, ceasing
further operation of the plugin.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

