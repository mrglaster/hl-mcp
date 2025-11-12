# StripWeapons
#### Syntax
```
enum /* Weapon types */
{
	Primary = 1
	, Secondary
	, Knife
	, Grenades
	, C4
};


stock StripWeapons(id, Type, bool: bSwitchIfActive = true)
```

#### Usage
id: | ```Player id```
---|---
type: | ```Weapon type (check enum below for types)```
bSwitchIfActive: | ```Switch to other weapon before stripping if stripped weapon is currently deployed```
#### Description
```
Strips a player's weapon based on type.
```

#### Return
```
: 1 on success, otherwise 0

Ex:  StripWeapons(id, Secondary);    // Strips secondary weapon with switching if deployed.
     StripWeapons(iPlayer, C4, false);   // Strips c4 without switching if deployed.
```


This code is a part of stripweapons.inc. To use this code you should include stripweapons.inc as ```#include <stripweapons>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.