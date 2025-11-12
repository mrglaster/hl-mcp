# show_activity_key
#### Syntax
```
stock show_activity_key(const KeyWithoutName[], const KeyWithName[], const ___AdminName[], any:...)
```

#### Usage
KeyWithoutName | ```The language key that does not have the name field.```
---|---
KeyWithName | ```The language key that does have the name field.```
__AdminName | ```The name of the person doing the action.```
... | ```Pass any extra format arguments for the language key in the variable arguments list.```
#### Description
```
Standard method to show activity to one single client with normal language keys.
These keys need to be in the format of standard AMXX keys:
  eg: ADMIN_KICK_1 = ADMIN: kick %s
      ADMIN_KICK_2 = ADMIN %s: kick %s
This depends on the amx_show_activity cvar.  See documentation for more details.
```

#### Return
```
This function has no return value.
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

