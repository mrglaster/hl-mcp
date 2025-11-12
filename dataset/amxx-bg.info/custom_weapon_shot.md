# custom_weapon_shot
#### Syntax
```
native custom_weapon_shot(weapon, index);
```

#### Usage
weapon | ```Custom weapon id```
---|---
index | ```Client index```
#### Description
```
Adds a shot event on a custom weapon to the internal stats.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the weapon id is not a custom weapon or an invalid client
index is provided, an error will be thrown.
```


This code is a part of csx.inc. To use this code you should include csx.inc as ```#include <csx>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).