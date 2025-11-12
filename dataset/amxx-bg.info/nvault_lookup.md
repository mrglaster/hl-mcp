# nvault_lookup
#### Syntax
```
native nvault_lookup(vault, const key[], value[], maxlen, &timestamp);
```

#### Usage
vault | ```A vault handle returned from nvault_open()```
---|---
key | ```A key to get information from```
value | ```A string where the value should be stored```
maxlen | ```Maximum length of the @value string```
timestamp | ```The timestamp of the entry```
#### Description
```
Retrieves full information about a vault entry.
```

#### Return
```
1 if an entry was found, 0 otherwise.
```

#### Error
```
On invalid vault handle.
```


This code is a part of nvault.inc. To use this code you should include nvault.inc as ```#include <nvault>```


  
  

