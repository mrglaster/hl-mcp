# menu_destroy
#### Syntax
```
native menu_destroy(menu);
```

#### Usage
menu | ```Menu resource identifier.```
---|---
#### Description
```
Destroys a menu.  Player menus will be cancelled (although may still linger
on the HUD), and future attempts to access the menu resource will result in
an error.

This must be called if you create menus dynamically, otherwise you will
leak memory.  For normal dynamic menus, you will destroy the menu in the
handler function (remembering to handle the case of a menu being cancelled,
it must still be destroyed).
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


  
  

