# client_built
#### Syntax
```
forward client_built(idPlayer, idStructure, type, impulse);
```

#### Usage
idPlayer | ```The player index who triggered the building.```
---|---
idStructure | ```The structure index that was created.```
type | ```The type of structure that was built (1 for marine, 2 for alien).```
impulse | ```The impulse command that was issued to build this structure.```
#### Description
```
Called whenever the client builds a structure.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).