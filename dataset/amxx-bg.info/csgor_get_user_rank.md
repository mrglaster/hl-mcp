# csgor_get_user_rank
#### Syntax
```
native csgor_get_user_rank(id, output[], len);
```

#### Usage
id | ```Player index.```
---|---
output | ```Output buffer for rang name.```
len | ```Max length of a output buffer.```
#### Description
```
Returns a player's Rank ID. Set Rang name in output.
```

#### Return
```
Player Rank ID. -1 on error. -2 if the player is not logged in.
```


This code is a part of csgo_remake.inc. To use this code you should include csgo_remake.inc as ```#include <csgo_remake>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.