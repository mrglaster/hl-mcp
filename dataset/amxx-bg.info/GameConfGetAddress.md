# GameConfGetAddress
#### Syntax
```
native GameConfGetAddress(GameConfig:handle, const name[]);
```

#### Usage
handle | ```Game config handle```
---|---
name | ```Name of the property to find```
#### Description
```
Finds an address calculation in a GameConfig file.
```

#### Return
```
An address calculated on success, otherwise 0 on failure.
```

#### Error
```
Invalid game config handle
```


This code is a part of gameconfig.inc. To use this code you should include gameconfig.inc as ```#include <gameconfig>```


  
  

