# menu_addblank2
#### Syntax
```
native menu_addblank2( menu );
```

#### Usage
menu | ```Menu resource identifier.```
---|---
#### Description
```
Adds a blank line to a menu, always shifting the numbering down.
```

#### Note
```
This will add a special item to create a blank line. It will affect the menu
item count and pagination. These items can be modified later but will ignore
access and item callback results.
```

#### Return
```
1 on success, 0 on failure.
```

#### Error
```
Invalid menu resource.
Too many items on non-paginated menu (max is 10)
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

