# menu_find_id
#### Syntax
```
native menu_find_id(menu, page, key);
```

#### Usage
menu | ```Menu resource identifier.```
---|---
page | ```Page on the menu.```
key | ```Key pressed (from 1 to 10).```
#### Description
```
Given a page on a menu and a keypress on that page, returns the item id selected.
If the item is less than 0, a special option was chosen (such as MENU_EXIT).
```

#### Return
```
Item identifier, or <0 for a special selection code.
```

#### Error
```
Invalid menu resource.
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

