# SetGlobalTransTarget
#### Syntax
```
native SetGlobalTransTarget(client);
```

#### Usage
client | ```Client index or LANG_SERVER```
---|---
#### Description
```
Sets the global language target.
```

#### Note
```
This is useful for creating functions
that will be compatible with the %l format specifier. Note that invalid
indexes can be specified but the error will occur during translation,
not during this function call.
```

#### Return
```
This function has no return value.
```


This code is a part of lang.inc. To use this code you should include lang.inc as ```#include <lang>```


  
  

