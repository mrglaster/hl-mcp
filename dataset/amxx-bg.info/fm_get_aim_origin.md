# fm_get_aim_origin
#### Syntax
```
stock fm_get_aim_origin(index, Float:origin[3]) {
```

#### Description

Writes aim origin to oring[3] array

```
// ported from AMXX's core get_user_origin(..., 3) (suggested by Greenberet)
stock fm_get_aim_origin(index, Float:origin[3]) {
	new Float:start[3], Float:view_ofs[3]
	pev(index, pev_origin, start)
	pev(index, pev_view_ofs, view_ofs)
	xs_vec_add(start, view_ofs, start)

	new Float:dest[3]
	pev(index, pev_v_angle, dest)
	engfunc(EngFunc_MakeVectors, dest)
	global_get(glb_v_forward, dest)
	xs_vec_mul_scalar(dest, 9999.0, dest)
	xs_vec_add(start, dest, dest)

	engfunc(EngFunc_TraceLine, start, dest, 0, index, 0)
	get_tr2(0, TR_vecEndPos, origin)

	return 1
}
```



This code is a part of fakemeta_util.inc. To use this code you should include fakemeta_util.inc as ```#include <fakemeta_util>```


  
  

