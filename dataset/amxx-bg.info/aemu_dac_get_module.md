# aemu_dac_get_module
#### Syntax
```
native bool:aemu_dac_get_module(output[], const lenght, bool:path = false);
```

#### Usage
output | ```Buffer to copy module name to```
---|---
lenght | ```Maximum buffer size```
path | ```Provides full path of the module name```
#### Description
```
Gets the DAC name of the suspicious module.
```

#### Note
```
: Use this native only inside the forward 'aemu_dac_query' and for reason 2,3 only
```

#### Return
```
return true if so, false otherwise
```


This code is a part of authemu.inc. To use this code you should include authemu.inc as ```#include <authemu>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.