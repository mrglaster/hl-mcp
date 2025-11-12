# fvault_load
#### Syntax
```
stock fvault_load(const vaultname[], Array:keys=Invalid_Array, Array:datas=Invalid_Array, Array:timestamps=Invalid_Array)
```

#### Usage
vaultname | ```- Vault name to look in```
---|---
keys | ```- cellarray holding all of the keys```
datas | ```- cellarray holding all of the data values```
timestamps | ```- cellarray holding all of the timestamps```
#### Description
```
Gets all vault keys, data, and timestamps
```

#### Return
```
Returns total number of entries in vault
```

#### Note
```
keys needs to be created like this: ArrayCreate(64)
         datas needs to be created like this: ArrayCreate(512)
         timestamps need to be created like this: ArrayCreate()
```


This code is a part of fvault.inc. To use this code you should include fvault.inc as ```#include <fvault>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.