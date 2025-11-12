# show_menu
#### Syntax
```
native show_menu(index, keys, const menu[], time = -1, const title[] = "");
```

#### Usage
index | ```Client to display menu to, use 0 to display to all clients```
---|---
keys | ```Enabled keys```
menu | ```Menu body```
time | ```Menu timeout in seconds, -1 to disable```
title | ```Name of the menu for internal tracking purposes```
#### Description
```
Displays a menu to the client.
```

#### Note
```
Keys is a bitflag value that represents which keys the user can press
on the menu. If you want to display disabled menu options, or skip
certain number slots, you should exclude that key from the bitflag.
amxconst.inc provides MENU_KEY_* constants for convenience.
```

#### Note
```
The title parameter is not displayed to the client and is only used for
identifying menus internally and assigning them to their callbacks.
The title corresponds to the menu name that you register with
register_menuid()
```

#### Return
```
1 on success, 0 if menu could not be displayed (client not
connected)
```

#### Error
```
If a single client is specified and the index is not within
the range of 1 to MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

