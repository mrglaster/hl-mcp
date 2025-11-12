# nvault_prune
#### Syntax
```
native nvault_prune(vault, start, end);
```

#### Usage
vault | ```A vault handle returned from nvault_open()```
---|---
start | ```The timestamp to start erasing from```
end | ```The timestamp to erase to```
#### Description
```
Prunes the vault for entries that are within the given timestamps.
```

#### Note
```
This will not erase values set with nvault_pset().
```

#### Note
```
An example of pruning all entries that are older than 24 hours:
nvault_prune(vaultHandle, 0, get_systime() - (60 * 60 * 24));
```

#### Return
```
Number of erased values.
```

#### Error
```
On invalid vault handle.
```


This code is a part of nvault.inc. To use this code you should include nvault.inc as ```#include <nvault>```


  
  

