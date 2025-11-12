# Functions in newmenus.inc
Function | Description  
---|---  
[menu_create](https://amxx-bg.info/api/newmenus/menu_create) | ```
Creates a new menu object.
```
  
[menu_makecallback](https://amxx-bg.info/api/newmenus/menu_makecallback) | ```
Creates a menu item callback handler.
```
  
[menu_additem](https://amxx-bg.info/api/newmenus/menu_additem) | ```
Adds an menu to a menu.
```
  
[menu_pages](https://amxx-bg.info/api/newmenus/menu_pages) | ```
Returns the number of pages in a menu.
```
  
[menu_items](https://amxx-bg.info/api/newmenus/menu_items) | ```
Returns the number of items in a menu.
```
  
[menu_display](https://amxx-bg.info/api/newmenus/menu_display) | ```
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
  
[menu_find_id](https://amxx-bg.info/api/newmenus/menu_find_id) | ```
Given a page on a menu and a keypress on that page, returns the item id selected.
If the item is less than 0, a special option was chosen (such as MENU_EXIT).
```
  
[menu_item_getinfo](https://amxx-bg.info/api/newmenus/menu_item_getinfo) | ```
Retrieves info about a menu item.
```
  
[menu_item_setname](https://amxx-bg.info/api/newmenus/menu_item_setname) | ```
Sets an item's display text.
```
  
[menu_item_setcmd](https://amxx-bg.info/api/newmenus/menu_item_setcmd) | ```
Sets an item's info string.
```
  
[menu_item_setcall](https://amxx-bg.info/api/newmenus/menu_item_setcall) | ```
Sets an item's callback.
```
  
[menu_item_setaccess](https://amxx-bg.info/api/newmenus/menu_item_setaccess) | ```
Sets an item's access.
```
  
[menu_destroy](https://amxx-bg.info/api/newmenus/menu_destroy) | ```
Destroys a menu.  Player menus will be cancelled (although may still linger
on the HUD), and future attempts to access the menu resource will result in
an error.

This must be called if you create menus dynamically, otherwise you will
leak memory.  For normal dynamic menus, you will destroy the menu in the
handler function (remembering to handle the case of a menu being cancelled,
it must still be destroyed).
```
  
[player_menu_info](https://amxx-bg.info/api/newmenus/player_menu_info) | ```
Returns information about a menu (if any) the client is currently viewing.
```
  
[menu_addblank](https://amxx-bg.info/api/newmenus/menu_addblank) | ```
Adds a blank line to a menu.
```
  
[menu_addtext](https://amxx-bg.info/api/newmenus/menu_addtext) | ```
Adds a text line to a menu.
```
  
[menu_addblank2](https://amxx-bg.info/api/newmenus/menu_addblank2) | ```
Adds a blank line to a menu, always shifting the numbering down.
```
  
[menu_addtext2](https://amxx-bg.info/api/newmenus/menu_addtext2) | ```
Adds a text line to a menu, always shifting the numbering down.
```
  
[menu_setprop](https://amxx-bg.info/api/newmenus/menu_setprop) | ```
Sets a menu property.
```
  
[menu_cancel](https://amxx-bg.info/api/newmenus/menu_cancel) | ```
Cancels a player's menu, effectively forcing the player to select MENU_EXIT.
The menu will still exist on their screen but any results are invalidated,
and the callback is invoked.
```
  

This code is a part of newmenus.inc. To use this code you should include newmenus.inc as ```#include <newmenus>```


  
  

