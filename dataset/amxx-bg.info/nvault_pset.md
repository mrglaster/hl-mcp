# nvault_pset
#### Syntax
```
native nvault_pset(vault, const key[], const value[]);
```

#### Usage
vault | ```A vault handle returned from nvault_open()```
---|---
key | ```A key to set the permanent value for```
value | ```A permanent value to set```
#### Description
```
Sets value of a vault entry and makes it permanent (non-erasable with nvault_prune()).
```

#### Note
```
A new entry is created if one with the given key doesn't exist.
```

#### Note
```
Permanent entries have no timestamp.
```

#### Return
```
This function has no return value.
```

#### Error
```
On invalid vault handle.
```


This code is a part of nvault.inc. To use this code you should include nvault.inc as ```#include <nvault>```


  
  

