# fm_get_user_gravity
#### Syntax
```
stock Float:fm_get_user_gravity(index) {
```

#### Description

Returns gravity value of player

```

stock Float:fm_get_user_gravity(index) {
	new Float:gravity
	pev(index, pev_gravity, gravity)

	return gravity
}

```


This code is a part of fakemeta_util.inc. To use this code you should include fakemeta_util.inc as ```#include <fakemeta_util>```


  
  

