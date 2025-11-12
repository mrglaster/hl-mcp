# fm_find_ent_by_integer
#### Syntax
```
stock fm_find_ent_by_integer(index, pev_field, value) {
```

#### Description

Finds entity by integer 

```
stock fm_find_ent_by_integer(index, pev_field, value) {
	static maxents
	if (!maxents)
		maxents = global_get(glb_maxEntities)

	for (new i = index + 1; i < maxents; ++i) {
		if (pev_valid(i) && pev(i, pev_field) == value)
			return i
	}

	return 0
}
```



This code is a part of fakemeta_util.inc. To use this code you should include fakemeta_util.inc as ```#include <fakemeta_util>```


  
  

