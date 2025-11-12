# fm_get_grenade_id
#### Syntax
```
stock fm_get_grenade_id(id, model[], len, grenadeid = 0) {
```

#### Description

Returns index of grenad the player owns

```
// note that for CS planted C4 has a "grenade" classname as well
stock fm_get_grenade_id(id, model[], len, grenadeid = 0) {
	new ent = fm_find_ent_by_owner(grenadeid, "grenade", id)
	if (ent && len > 0)
		pev(ent, pev_model, model, len)

	return ent
}
```


This code is a part of fakemeta_util.inc. To use this code you should include fakemeta_util.inc as ```#include <fakemeta_util>```


  
  

