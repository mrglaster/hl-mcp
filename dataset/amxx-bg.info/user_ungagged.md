# user_ungagged
#### Syntax
```
forward user_ungagged(id)
```

#### Usage
id | ```Index of the ungagged player```
---|---
#### Description
```
Called when player got ungagged
```

#### Note
```
This forward is called only on alive clients. If player has been ungagged
while not in the server, the forward won't get called.
```

#### Note
```
This forward is also called when player's gag has expired.
```

#### Return
```
This forward ignores the returned value
```


This code is a part of gagsystem.inc. To use this code you should include gagsystem.inc as ```#include <gagsystem>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.