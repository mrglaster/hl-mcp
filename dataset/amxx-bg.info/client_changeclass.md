# client_changeclass
#### Syntax
```
forward client_changeclass(id, newclass, oldclass);
```

#### Usage
id | ```The index of the player who changed.```
---|---
newclass | ```The class the client changed to.  Check the class enum in ns_const.inc.```
oldclass | ```The class the client changed from.  Check the class enum in ns_const.inc.```
#### Description
```
Called whenever the client's class is changed.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).