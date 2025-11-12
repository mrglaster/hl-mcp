# cs_set_hud_icon
#### Syntax
```
stock cs_set_hud_icon(id, active = 0, sprite[] = "", alpha = 100, flashrate = 0, flashdelay = 0, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
active | ```If set to 0, it will remove the scenario icon and ignore all other arguments. Always set this to 1 if you want to use any of the other arguments```
sprite | ```Sprite name (valid names are listed in sprites.hud.txt)```
alpha | ```Sprite alpha (100-255)```
flashrate | ```If nonzero, the sprite will flash from the given alpha in the "alpha" argument to an alpha of 100, at a rate set in this argument```
flashdelay | ```Delay (in seconds) between each flash```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Displays a sprite to the right side of the round timer.
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