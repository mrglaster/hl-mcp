# AddMenuItem
#### Syntax
```
stock AddMenuItem(const MENU_TEXT[], const MENU_CMD[], const MENU_ACCESS, const MENU_PLUGIN[])
```

#### Usage
MENU_TEXT | ```Item text that will be displayed in the menu```
---|---
MENU_CMD | ```Command that will be executed on the client```
MENU_ACCESS | ```Admin access required for menu command```
MENU_PLUGIN | ```Case-insensitive name or filename of plugin providing the menu command```
#### Description
```
Adds a menu item/command to the admin menu (amxmodmenu) handled by the
"Menus Front-End" plugin, if it is loaded.
```

#### Return
```
This function has no return value.
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

