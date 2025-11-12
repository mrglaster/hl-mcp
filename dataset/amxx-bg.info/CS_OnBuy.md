# CS_OnBuy
#### Syntax
```
forward CS_OnBuy(index, item);
```

#### Usage
index | ```Client index```
---|---
item | ```Item id```
#### Description
```
Called when a client purchases an item.
```

#### Note
```
This is called right before the user receives the item and before the
money is deducted from their cash reserves.
```

#### Note
```
For a list of possible item ids see the CSI_* constants.
```

#### Return
```
PLUGIN_CONTINUE to let the buy continue
PLUGIN_HANDLED to block the buy
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).