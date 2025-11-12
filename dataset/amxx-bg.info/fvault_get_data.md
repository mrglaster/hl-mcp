# fvault_get_data
#### Syntax
```
stock fvault_get_data(const vaultname[], const key[], data[], len, &timestamp=0)
```

#### Usage
vaultname | ```Vault name to look in```
---|---
key | ```Key name to look for the data```
data | ```String which data will be copied to```
len | ```Length of data```
timestamp | ```The unix time of when the data was last set ( -1 if permanent data, 0 if old fvault version ) ( optional param )```
#### Description
```
Retrieves data specified by a key
```

#### Return
```
Returns 1 on success, 0 on failue.
```


This code is a part of fvault.inc. To use this code you should include fvault.inc as ```#include <fvault>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.