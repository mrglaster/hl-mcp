# GameConfGetClassOffset
#### Syntax
```
native GameConfGetClassOffset(GameConfig:handle, const classname[], const key[]);
```

#### Usage
handle | ```Game config handle```
---|---
classname | ```Class name to match from the offset section```
key | ```Key to retrieve from the offset section```
#### Description
```
Returns an offset value given a classname.
```

#### Return
```
An offset, or -1 on failure
```

#### Error
```
Invalid game config handle
```


This code is a part of gameconfig.inc. To use this code you should include gameconfig.inc as ```#include <gameconfig>```


  
  

