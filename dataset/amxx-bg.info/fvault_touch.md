# fvault_touch
#### Syntax
```
stock fvault_touch(const vaultname[], const key[], const timestamp=-1)
```

#### Usage
vaultname | ```Vault name to look in```
---|---
key | ```Key to update timestamp (if it doesn't exist, a blank value will be set)```
timestamp | ```Unix Time to set for the key (-1 for current time)```
#### Description
```
Updates the timestamp on a key located within the vault
```

#### Return
```
Returns 2 on new entry, 1 on success, 0 on failure for the key having a permanent timestamp
```


This code is a part of fvault.inc. To use this code you should include fvault.inc as ```#include <fvault>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.