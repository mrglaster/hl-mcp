# hide_hud_elements
#### Syntax
```
stock hide_hud_elements(id, HideElemenentFlags:elements, bool:noadd = true, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
elements | ```HUD elements to hide. The names are self-explanatory:   HideElement_Cross_Ammo_WPNList   HideElement_Flashlight (+)   HideElement_All   HideElement_Radar_Health_Armor (+)   HideElement_Timer (+)   HideElement_Money (+)   HideElement_Crosshair```
noadd | ```If set to false and the chosen element names have a "+" sign, an additional crosshair will be drawn.```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Hides specific elements from the HUD.
```

#### Note
```
The symbol + means that an additional crosshair will be drawn.
This crosshair looks not like the regular one, but like the one that
is drawn in spectator mode. You can remove this crosshair by setting
the "noadd" argument to "true".
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.