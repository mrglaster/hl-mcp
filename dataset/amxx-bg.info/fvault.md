# Functions in fvault.inc
Function | Description  
---|---  
[fvault_get_keyname](https://amxx-bg.info/api/fvault/fvault_get_keyname) | ```
Retrieves a key name specified by its number
```
  
[fvault_get_keynum](https://amxx-bg.info/api/fvault/fvault_get_keynum) | ```
Retrieves a key number specified by its name
```
  
[fvault_get_data](https://amxx-bg.info/api/fvault/fvault_get_data) | ```
Retrieves data specified by a key
```
  
[fvault_set_data](https://amxx-bg.info/api/fvault/fvault_set_data) | ```
Sets data of a key with current timestamp
```
  
[fvault_pset_data](https://amxx-bg.info/api/fvault/fvault_pset_data) | ```
Sets data of a key permanently (can't be removed with fvault_prune)
```
  
[fvault_remove_key](https://amxx-bg.info/api/fvault/fvault_remove_key) | ```
Removes a key from a vault
```
  
[fvault_prune](https://amxx-bg.info/api/fvault/fvault_prune) | ```
Prunes the vault for keys that are within the given timestamps
```
  
[fvault_touch](https://amxx-bg.info/api/fvault/fvault_touch) | ```
Updates the timestamp on a key located within the vault
```
  
[fvault_size](https://amxx-bg.info/api/fvault/fvault_size) | ```
Retrieves total keys located within the vault
```
  
[fvault_clear](https://amxx-bg.info/api/fvault/fvault_clear) | ```
Clears all key entries for a vault
```
  
[fvault_get_vaultname](https://amxx-bg.info/api/fvault/fvault_get_vaultname) | ```
Retrieves a vault name specified by its number
```
  
[fvault_get_vaultnum](https://amxx-bg.info/api/fvault/fvault_get_vaultnum) | ```
Retrieves a vault number specified by its name
```
  
[fvault_total](https://amxx-bg.info/api/fvault/fvault_total) | ```
Retrieves total vaults ever created
```
  
[fvault_load](https://amxx-bg.info/api/fvault/fvault_load) | ```
Gets all vault keys, data, and timestamps
```
  
[_FormatVaultName](https://amxx-bg.info/api/fvault/_FormatVaultName) | ```
This function has no description.
```
  

This code is a part of fvault.inc. To use this code you should include fvault.inc as ```#include <fvault>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.