# crxranks_give_user_xp
#### Syntax
```
native crxranks_give_user_xp(id, amount = 0, reward[] = "", CRXRanks_XPSources:source = CRXRANKS_XPS_PLUGIN)
```

#### Usage
id | ```Client index.```
---|---
amount | ```XP amount.```
reward | ```Reward keyword.```
source | ```XP source.```
#### Description
```
Gives a specific amount of XP to the client.
```

#### Note
```
If the "reward" parameter is set, the plugin will ignore the amount set
in the "amount" parameter and will attempt to give the XP set in the
configuration file by the specific keyword set in the "reward" parameter.
```

#### Return
```
Amount of XP given.
```


This code is a part of crxranks.inc. To use this code you should include crxranks.inc as ```#include <crxranks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.