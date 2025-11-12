# rg_observer_find_next_player
#### Syntax
```
native rg_observer_find_next_player(const player, const bool:bReverse = false, const name[] = "");
```

#### Usage
player | ```Player index.```
---|---
bReverse | ```If bReverse is true, finding order will be reversed```
name | ```Player name to find.```
#### Description
```
Call origin function CBasePlayer::Observer_FindNextPlayer()
```

#### Note
```
Player must be a valid observer (m_afPhysicsFlags & PFLAG_OBSERVER).
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.