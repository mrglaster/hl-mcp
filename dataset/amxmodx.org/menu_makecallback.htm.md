enu_makecallback
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
menu_makecallback - Creates a menu item callback handler. 
Syntax
menu_makecallback ( function[] ) 
Type
Native 
Notes
The callback handler is passed the playerid, menuid, and itemid. It can return ITEM_IGNORE, ITEM_ENABLED, or ITEM_DISABLED.
