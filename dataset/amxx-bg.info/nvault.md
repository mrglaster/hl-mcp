# Functions in nvault.inc
Function | Description  
---|---  
[nvault_open](https://amxx-bg.info/api/nvault/nvault_open) | ```
Opens a vault by name. Creates a vault if it doesn't exist yet.
```
  
[nvault_get](https://amxx-bg.info/api/nvault/nvault_get) | ```
Retrieves a value from the given key.
```
  
[nvault_lookup](https://amxx-bg.info/api/nvault/nvault_lookup) | ```
Retrieves full information about a vault entry.
```
  
[nvault_set](https://amxx-bg.info/api/nvault/nvault_set) | ```
Sets value of a vault entry and updates the timestamp.
```
  
[nvault_pset](https://amxx-bg.info/api/nvault/nvault_pset) | ```
Sets value of a vault entry and makes it permanent (non-erasable with nvault_prune()).
```
  
[nvault_prune](https://amxx-bg.info/api/nvault/nvault_prune) | ```
Prunes the vault for entries that are within the given timestamps.
```
  
[nvault_close](https://amxx-bg.info/api/nvault/nvault_close) | ```
Closes a vault.
```
  
[nvault_remove](https://amxx-bg.info/api/nvault/nvault_remove) | ```
Removes an entry from the vault by its key.
```
  
[nvault_touch](https://amxx-bg.info/api/nvault/nvault_touch) | ```
"Touches" an entry in the vault, updating its timestamp.
```
  

This code is a part of nvault.inc. To use this code you should include nvault.inc as ```#include <nvault>```


  
  

