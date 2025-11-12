# ns_get_build
#### Syntax
```
native ns_get_build(const classname[],builtOnly=1,Number=0);
```

#### Description
```
Returns built/unbuilt structures.
If:
builtOnly is 1 (default):
Only fully built structures are counted.
builtOnly is 0:
Any structure meeting the classname is counted.

Number is 0 (default):
The total number of matching structures is returned.
Number is any other value:
The index of the #th matching structure is returned.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).