# LocatePlayer
#### Syntax
```
stock LocatePlayer(id, const identStr[], const pluginTag[], LocatePlayerFlags:flags = LP_OBEY_IMMUNITY)
```

#### Description
```
Finds player index based on Steam ID, partial player name, user IP or user ID.
```

#### Note
```
Function outputs information in console if player is not located.
```

#### Return
```
-1 if player is not found or multiple players found or found player doesn't match options given via flags
index of located player on success.
```


This code is a part of common_functions.inc. To use this code you should include common_functions.inc as ```#include <common_functions>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.