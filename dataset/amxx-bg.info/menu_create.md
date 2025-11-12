# menu_create
#### Syntax
```
native menu_create(const title[], const handler[], bool:ml = false);
```

#### Usage
title | ```Title the menu should use.```
---|---
handler | ```Name of the handler function.  The function will be invoked once and only once to every menu_display() call.```
ml | ```If true, the menu title and items will be looked up as multilingual keys when the menu displays.```
#### Description
```
Creates a new menu object.
```

#### Note
```
The handler function should be prototyped as:

public <function>(id, menu, item)
  id     - Client the menu is being acted upon.
  menu   - Menu resource identifier.
  item   - Item the client selected.  If less than 0, the menu was
     cancelled and the item is a status code.  menu_display
     should never be called immediately if the item is a status
     code, for re-entrancy reasons.
```

#### Note
```
The handler function should always return PLUGIN_HANDLED to block
any old menu handlers from potentially feeding on the menu, unless
that is the desired functionality.
```

#### Return
```
Menu resource identifier which must be destroyed via
menu_destroy().  All menus are destroyed when the plugin
unloads.
```

#### Error
```
Function name not found.
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

