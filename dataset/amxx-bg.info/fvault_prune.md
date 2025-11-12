# fvault_prune
#### Syntax
```
stock fvault_prune(const vaultname[], const start=-1, const end=-1)
```

#### Usage
vaultname | ```Vault name to look in```
---|---
start | ```If timestamp is after this Unix Time (set -1 to prune from very start)```
end | ```If timestamp is before this Unix Time (set -1 to prune to most time)```
#### Description
```
Prunes the vault for keys that are within the given timestamps
```

#### Return
```
Returns number of keys pruned
```


This code is a part of fvault.inc. To use this code you should include fvault.inc as ```#include <fvault>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.