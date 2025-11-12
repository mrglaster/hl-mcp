# menu_cancel
#### Syntax
```
native menu_cancel(player);
```

#### Usage
player | ```Client index.```
---|---
#### Description
```
Cancels a player's menu, effectively forcing the player to select MENU_EXIT.
The menu will still exist on their screen but any results are invalidated,
and the callback is invoked.
```

#### Return
```
This function has no return value.
```

#### Error
```
Invalid client index.
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

