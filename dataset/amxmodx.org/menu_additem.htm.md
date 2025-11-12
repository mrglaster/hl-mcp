enu_additem
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
menu_additem - Adds an item to a menu. When displayed, the name will be shown. 
Syntax
menu_additem ( menu, const name[], const command[], paccess=0, callback=-1 ) 
Type
Native 
Notes
If the player does not have the access it is disabled. If you set callback, the callback will be called before the item is printed on the screen. This lets you change it real time based on conditions.
