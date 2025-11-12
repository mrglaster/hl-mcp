# client_putinserver
#### Syntax
```
forward client_putinserver(id);
```

#### Usage
id | ```Client index```
---|---
#### Description
```
Called when a client is entering the game.
```

#### Note
```
It is not defined whether the client already has a SteamID when this
forward is called. client_authorized may occur either before or after
this.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

