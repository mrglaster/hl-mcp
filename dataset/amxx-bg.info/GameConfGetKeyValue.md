# GameConfGetKeyValue
#### Syntax
```
native bool:GameConfGetKeyValue(GameConfig:handle, const key[], buffer[], maxlen);
```

#### Usage
handle | ```Game config handle```
---|---
key | ```Key to retrieve from the Keys section```
buffer | ```Destination string buffer```
maxlen | ```Maximum length of output string buffer```
#### Description
```
Gets the value of a key from the "Keys" section.
```

#### Return
```
True if key existed, false otherwise
```

#### Error
```
Invalid game config handle
```


This code is a part of gameconfig.inc. To use this code you should include gameconfig.inc as ```#include <gameconfig>```


  
  

