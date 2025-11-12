# aemu_set_filter_cvar
#### Syntax
```
native aemu_set_filter_cvar(const index, const name[], const Float:value /*const Float:min*/, const Float:max = -999.0 /* unset */);
```

#### Usage
index | ```Client index```
---|---
name | ```CVar name```
value | ```CVar value```
max | ```The max threshold value of CVar```
#### Description
```
Set's CVar filter that a client obliged to adhere is specified.
```

#### Note
```
Set to 0 for use common filter
```

#### Optional
```
Use min/max params instead value param for the same purpose,
but with clamp filter as 'aemu_set_filter_cvar(id, "ex_interp", 0.01, 0.1)'
```

#### Note
```
If param is specified, then value param it's min threshold
```

#### Return
```
This function has no return value.
```


This code is a part of authemu.inc. To use this code you should include authemu.inc as ```#include <authemu>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.