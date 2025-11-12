# cs_get_translated_item_alias
#### Syntax
```
native bool:cs_get_translated_item_alias(const alias[], itemname[], maxlength);
```

#### Usage
alias | ```Alias name```
---|---
itemname | ```Buffer to store item name to```
maxlength | ```Maximum buffer size```
#### Description
```
Returns an item name associated with a command alias.
```

#### Note
```
The alias is case sensitive.
```

#### Note
```
If not an alias to a weapon, buffer will be set with the original alias.
```

#### Return
```
True if alias is translated, false otherwise
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).