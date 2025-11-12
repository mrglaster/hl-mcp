# fm_get_speed
#### Syntax
```
stock fm_get_speed(entity) {
```

#### Description

Retrieves speed of an entity 

```
stock fm_get_speed(entity) {
	new Float:Vel[3]
	pev(entity, pev_velocity, Vel)

	return floatround(vector_length(Vel))
}
```


This code is a part of fakemeta_util.inc. To use this code you should include fakemeta_util.inc as ```#include <fakemeta_util>```


  
  

