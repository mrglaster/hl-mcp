# draw_item_pickup_icon
#### Syntax
```
stock draw_item_pickup_icon(id, itemname[], bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
itemname | ```Item name```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Temporarily draws a corresponding item HUD icon in the middle of the
right side of the screen.
```

#### Note
```
This stock isn't available in Day of Defeat.
```

#### Note
```
Draw time depends on the hud_drawhistory_time client cvar value.
```

#### Note
```
A list of all icons and screenshots of them can be found here:
http://doktor.haze.free.fr/counter-strike/sprites_screens/index.php
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.