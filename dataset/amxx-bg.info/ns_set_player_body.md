# ns_set_player_body
#### Syntax
```
native ns_set_player_body(id, body=-1);
```

#### Usage
id | ```The player id to change.```
---|---
body | ```The body number to change to.```
#### Description
```
Sets a player body.  Omit the second parameter to return to default
```

#### Note
```
The body does not revert on death, teamswitch, gestation, etc.
```

#### Return
```
This function has no return value.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).