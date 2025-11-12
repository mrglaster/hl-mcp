# fm_find_ent_by_flags
#### Syntax
```
stock fm_find_ent_by_flags(index, pev_field, flags) {
```

#### Description

Implementation of stock, that finds some entity by pev and flags 

```
stock fm_find_ent_by_flags(index, pev_field, flags) {
	static maxents
	if (!maxents)
		maxents = global_get(glb_maxEntities)

	for (new i = index + 1; i < maxents; ++i) {
		if (pev_valid(i) && (pev(i, pev_field) & flags) == flags)
			return i
	}

	return 0
}
```

This code is a part of fakemeta_util.inc. To use this code you should include fakemeta_util.inc as ```#include <fakemeta_util>```


  
  

