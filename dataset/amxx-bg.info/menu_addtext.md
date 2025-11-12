# menu_addtext
#### Syntax
```
native menu_addtext(menu, const text[], slot=1);
```

#### Usage
menu | ```Menu resource identifier.```
---|---
text | ```Text to add.```
slot | ```1 (default) if the line should shift the numbering down. 0 if the line should be a visual shift only.```
#### Description
```
Adds a text line to a menu.
```

#### Note
```
When using slot=1 this might break your menu. To achieve this functionality
menu_addtext2 should be used.
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


  
  

