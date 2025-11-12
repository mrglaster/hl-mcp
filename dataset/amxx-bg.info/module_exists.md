# module_exists
#### Syntax
```
native module_exists(const logtag[]);
```

#### Usage
logtag | ```Module shortname```
---|---
#### Description
```
Returns if a specific module is loaded.
```

#### Note
```
This uses the same method AMXX uses internally to see if a module is
required by a plugin.
```

#### Note
```
Example usage: module_exists("cstrike")
```

#### Return
```
1 if module is loaded, 0 otherwise
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

