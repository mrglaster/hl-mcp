# csgor_get_user_stattrack
#### Syntax
```
native csgor_get_user_stattrack(id, WeaponID, skinname[], len);
```

#### Usage
id | ```Player index.```
---|---
WeaponID | ```Weapon index.```
skinname | ```Buffer to copy name of the StatTrack skin name.```
len | ```Buffer lenght.```
#### Description
```
Stores player's applied StatTrack skin name into a string.
```

#### Return
```
-1 if player is not within range, if player is not logged into his account or WeaponID is not within range.
```


This code is a part of csgo_remake.inc. To use this code you should include csgo_remake.inc as ```#include <csgo_remake>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.