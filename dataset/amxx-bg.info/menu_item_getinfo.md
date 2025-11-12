# menu_item_getinfo
#### Syntax
```
native menu_item_getinfo(menu, item, &access = 0, info[] = "", infolen = 0, name[]="", namelen=0, &callback = 0);
```

#### Usage
menu | ```Menu resource identifier.```
---|---
item | ```Item identifier.```
access | ```Variable to store access value.```
info | ```Buffer to store item info.```
infolen | ```Item info buffer length.```
name | ```Buffer to store item display text.```
namelen | ```Item name buffer length.```
callback | ```Callback ID.```
#### Description
```
Retrieves info about a menu item.
```

#### Return
```
1 on success, 0 on failure.
```

#### Error
```
Invalid menu resource.
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

