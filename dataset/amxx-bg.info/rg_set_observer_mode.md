# rg_set_observer_mode
#### Syntax
```
native rg_set_observer_mode(const player, const mode);
```

#### Usage
player | ```Player index.```
---|---
mode | ```Observer mode, see OBS_* constants in cssdk_const.inc```
#### Description
```
Sets player current Observer mode.
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