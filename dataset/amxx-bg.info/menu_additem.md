# menu_additem
#### Syntax
```
native menu_additem(menu, const name[], const info[]="", paccess=0, callback=-1);
```

#### Usage
menu | ```Menu resource identifier.```
---|---
name | ```Item text to display.```
info | ```Item info string for internal information.```
paccess | ```Access required by the player viewing the menu.```
callback | ```If set to a valid ID from menu_makecallback(), the callback will be invoked before drawing the item.```
#### Description
```
Adds an menu to a menu.
```

#### Return
```
This function has no return value.
```

#### Error
```
Invalid menu resource.
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

