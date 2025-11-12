# nvault_open
#### Syntax
```
native nvault_open(const name[]);
```

#### Usage
name | ```Name of the vault. The vault will be created in ${amxx_datadir}/vault directory.```
---|---
#### Description
```
Opens a vault by name. Creates a vault if it doesn't exist yet.
```

#### Return
```
The vault handle to be used in other natives.
INVALID_HANDLE (-1) if not successfully opened.
```


This code is a part of nvault.inc. To use this code you should include nvault.inc as ```#include <nvault>```


  
  

