# nvault_set
#### Syntax
```
native nvault_set(vault, const key[], const value[]);
```

#### Usage
vault | ```A vault handle returned from nvault_open()```
---|---
key | ```A key to set the value for```
value | ```A value to set```
#### Description
```
Sets value of a vault entry and updates the timestamp.
```

#### Note
```
A new entry is created if one with the given key doesn't exist.
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


  
  

