# nvault_touch
#### Syntax
```
native nvault_touch(vault, const key[], timestamp=-1);
```

#### Usage
vault | ```A vault handle returned from nvault_open()```
---|---
key | ```The key to search for```
timestamp | ```Update an entry's timestamp to this one. Default is -1.```
#### Description
```
"Touches" an entry in the vault, updating its timestamp.
```

#### Note
```
If timestamp is equal to -1, it will use the current time.
```

#### Note
```
An empty entry is created if one with the given key doesn't exist.
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


  
  

