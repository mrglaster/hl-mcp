# is_user_gagged
#### Syntax
```
native is_user_gagged(id, print = 0)
```

#### Usage
id | ```Client index```
---|---
print | ```Should gag info be printed to the target player```
#### Description
```
Checks if player is gagged
```

#### Return
```
Returns 1 if player is gagged otherwise 0
```

#### Error
```
If the index is not within the range of 1 to MaxClients or
the client is not connected, an error will be thrown.
```


This code is a part of gagsystem.inc. To use this code you should include gagsystem.inc as ```#include <gagsystem>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.