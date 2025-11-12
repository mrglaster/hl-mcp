# menu_makecallback
#### Syntax
```
native menu_makecallback(const function[]);
```

#### Usage
function | ```Function name.```
---|---
#### Description
```
Creates a menu item callback handler.
```

#### Note
```
The handler function should be prototyped as:

public <function>(id, menu, item)
  id      - Client index being displayed to.
  menu    - Menu resource identifier.
  item    - Item being drawn.
  <return> - ITEM_IGNORE to use the default functionality.  ITEM_ENABLED to
       explicitly enable or ITEM_DISABLED to explicitly disable.
```

#### Return
```
Menu callback ID.
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

