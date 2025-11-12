# rg_get_global_iteminfo
#### Syntax
```
native rg_get_global_iteminfo(const {WeaponIdType,_}:weapon_id, ItemInfo:type, any:...);
```

#### Usage
weapon_id | ```Weapon id, see WEAPON_* constants```
---|---
type | ```Item info type. See ItemInfo constants.```
#### Description
```
Gets a parameter of the global CBasePlayerItem::m_ItemInfoArray array
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.