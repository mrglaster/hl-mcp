# menu_item_setcall
#### Syntax
```
native menu_item_setcall(menu, item, callback=-1);
```

#### Usage
menu | ```Menu resource identifier.```
---|---
item | ```Item identifier.```
callback | ```New callback from menu_makecallback(), or -1 to clear.```
#### Description
```
Sets an item's callback.
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


  
  

