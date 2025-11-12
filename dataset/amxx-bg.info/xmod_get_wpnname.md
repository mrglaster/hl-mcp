# xmod_get_wpnname
#### Syntax
```
native xmod_get_wpnname(wpnindex, name[], len);
```

#### Usage
wpnindex | ```Weapon id```
---|---
name | ```Buffer to copy weapon name to```
len | ```Maximmum buffer size```
#### Description
```
Retrieves the full weapon name of a weapon id.
```

#### Note
```
For a list of default CS weapon ids see the CSW_* constants in
amxconst.inc, this function also works on custom weapons.
```

#### Note
```
For the default CS weapons this obviously returns true only for
CSW_KNIFE.
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If an invalid weapon id is provided an error will be thrown.
```


This code is a part of csx.inc. To use this code you should include csx.inc as ```#include <csx>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).