# LibraryExists
#### Syntax
```
native LibraryExists(const library[], LibType:type);
```

#### Usage
library | ```Library/Class shortname```
---|---
type | ```Type to search for```
#### Description
```
Returns if a specific library or class is loaded.
```

#### Note
```
This is the newer version of module_exists(), enabling users to
distinguish between libraries and classes, while module_exists() always
checks for both types.
```

#### Note
```
For a list of possible types, see the LibType enum in amxconst.inc
```

#### Return
```
1 if module is loaded, 0 otherwise
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

