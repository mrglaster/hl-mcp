# fm_get_user_longjump
#### Syntax
```
stock bool:fm_get_user_longjump(index) {
```

#### Description

Checks if player has the longjump

```
stock bool:fm_get_user_longjump(index) {
	new value[2]
	engfunc(EngFunc_GetPhysicsKeyValue, index, "slj", value, 1)
	switch (value[0]) {
		case '1': return true
	}

	return false
}
```

This code is a part of fakemeta_util.inc. To use this code you should include fakemeta_util.inc as ```#include <fakemeta_util>```


  
  

