# menu_display
#### Syntax
```
native menu_display(id, menu, page=0, time=-1);
```

#### Usage
id | ```Client index.```
---|---
menu | ```Menu resource identifier.```
page | ```Page to start from (starting from 0).```
time | ```If >=0 menu will timeout after this many seconds```
#### Description
```
Displays a menu to one client.  This should never be called from a handler
when the item is less than 0 (i.e. calling this from a cancelled menu will
result in an error).

Starting with 1.8.3 this allows to specify a menu timeout similar to the
show_menu native. If the menu exists on the client past the timeout *any*
further action will send the MENU_TIMEOUT status code to the menu handler.
That includes actions which would otherwise send MENU_EXIT, such as the
client selecting an item or disconnecting and calling menu_cancel or
menu_destroy on a live menu.
```

#### Return
```
This function has no return value.
```

#### Error
```
Invalid menu resource or client index.
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

