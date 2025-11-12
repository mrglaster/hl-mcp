# CloseGameConfigFile
#### Syntax
```
native CloseGameConfigFile(&GameConfig:handle);
```

#### Usage
handle | ```Game config handle```
---|---
#### Description
```
Destroys a game config and frees its memory.
```

#### Note
```
The function automatically sets the variable passed to it to 0 to aid
in preventing accidental usage after destroy.
```

#### Return
```
1 on success, 0 if an invalid handle was passed in
```


This code is a part of gameconfig.inc. To use this code you should include gameconfig.inc as ```#include <gameconfig>```


  
  

