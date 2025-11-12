# player_menu_info
#### Syntax
```
native player_menu_info(id, &menu, &newmenu, &menupage=0);
```

#### Usage
id | ```Client index.```
---|---
menu | ```Variable to store old menu id.  If none, then <1 will be stored.```
newmenu | ```Variable to store new menu id.  If none, then -1 will be stored.```
menupage | ```Variable to store current page of the new menu, if any.```
#### Description
```
Returns information about a menu (if any) the client is currently viewing.
```

#### Note
```
If newmenu is valid, then the menu will refer to the menuid associated with
the title. If newmenu is not valid, and the menu is valid, then the player
is viewing a menu displayed with show_menu().
```

#### Note
```
Both may be invalid if the player is not viewing a menu.
```

#### Return
```
1 if the player is viewing a menu, 0 otherwise.
```

#### Error
```
Invalid client.
```


This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

