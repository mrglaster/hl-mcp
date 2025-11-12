# CS_OnBuyAttempt
#### Syntax
```
forward CS_OnBuyAttempt(index, item);
```

#### Usage
index | ```Client index```
---|---
item | ```Item id```
#### Description
```
Called when a client attempts to purchase an item.
```

#### Note
```
This is called immediately when the client issues a buy command. The
game has not yet checked if the client can actually buy the weapon.
```

#### Note
```
For a list of possible item ids see the CSI_* constants.
```

#### Return
```
PLUGIN_CONTINUE to let the buy attempt continue
PLUGIN_HANDLED to block the buy attempt
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).