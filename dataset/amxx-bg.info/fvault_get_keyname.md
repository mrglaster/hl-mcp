# fvault_get_keyname
#### Syntax
```
stock fvault_get_keyname(const vaultname[], const keynum, key[], len)
```

#### Usage
vaultname | ```Vault name to look in```
---|---
keynum | ```Key number within the vault to find key name```
key | ```String which key name will be copied to```
len | ```Length of key name```
#### Description
```
Retrieves a key name specified by its number
```

#### Return
```
Returns 1 on success, 0 on failue.
```


This code is a part of fvault.inc. To use this code you should include fvault.inc as ```#include <fvault>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.