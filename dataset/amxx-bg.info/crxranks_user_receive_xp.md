# crxranks_user_receive_xp
#### Syntax
```
forward crxranks_user_receive_xp(id, xp, CRXRanks_XPSources:source)
```

#### Usage
id | ```Client index.```
---|---
xp | ```Amount of XP ready to be received.```
source | ```The XP source.```
#### Description
```
Called right before the client receives XP.
```

#### Return
```
CRXRANKS_STOP to prevent the XP from being added,
CRXRANKS_CONTINUE to let the XP pass through,
any integer value to modify the amount of XP that
is going to be received
```


This code is a part of crxranks.inc. To use this code you should include crxranks.inc as ```#include <crxranks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.