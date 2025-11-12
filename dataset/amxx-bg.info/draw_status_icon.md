# draw_status_icon
#### Syntax
```
stock draw_status_icon(id, sprite[] = "", StatusIconFlags:status = StatusIcon_Hide, r = 0, g = 0, b = 0, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
sprite | ```Sprite name (valid names are listed in sprites/hud.txt)```
status | ```Valid status values:   StatusIcon_Hide         - hides the status icon   StatusIcon_Show         - shows the status icon   StatusIcon_Flash        - flashes the status icon```
r | ```Red color amount (0 - 255)```
g | ```Green color amount (0 - 255)```
b | ```Blue color amount (0 - 255)```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Draws a specified status HUD icon.
```

#### Note
```
This stock is available only in the following games:
  Counter-Strike
  Counter-Strike: Condition Zero
  Half-Life: Opposing Force
  Team Fortress Classic
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