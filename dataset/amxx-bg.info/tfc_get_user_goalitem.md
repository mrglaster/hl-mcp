# tfc_get_user_goalitem
#### Syntax
```
native tfc_get_user_goalitem(index, &team);
```

#### Description
```
Returns 1 if user is carrying a goal item such as a flag or a keycard, else 0.
Team is by reference parameter that will be set to owning team(s) of the goal item.
Use the TFC_GOALITEM_* constants to determine the owning team.
```


This code is a part of tfcx.inc. To use this code you should include tfcx.inc as ```#include <tfcx>```


  
  

Warning: This include is compatible only with Team Fortress: Classic and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).