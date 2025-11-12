# Functions in amxmisc.inc
Function | Description  
---|---  
[is_user_admin](https://amxx-bg.info/api/amxmisc/is_user_admin) | ```
Returns if the client has any admin flags set
```
  
[cmd_access](https://amxx-bg.info/api/amxmisc/cmd_access) | ```
Returns if the user can execute the current command by checking the necessary
admin flags and parameter count. Displays a denied access message to the user
if missing privileges or a usage example if too few parameters are provided.
```
  
[access](https://amxx-bg.info/api/amxmisc/access) | ```
Returns if the client has the specified admin flags.
```
  
[cmd_target](https://amxx-bg.info/api/amxmisc/cmd_target) | ```
Processes a generic target pattern and tries to match it to a client based
on filtering flags. If no unique target is found an appropriate message is
displayed to the admin.
```
  
[show_activity](https://amxx-bg.info/api/amxmisc/show_activity) | ```
Standard method to show admin activity to clients connected to the server.
This depends on the amx_show_activity cvar. See documentation for more details.
```
  
[show_activity_id](https://amxx-bg.info/api/amxmisc/show_activity_id) | ```
Standard method to show admin activity to a single client.
This depends on the amx_show_activity cvar. See documentation for more details.
```
  
[show_activity_key](https://amxx-bg.info/api/amxmisc/show_activity_key) | ```
Standard method to show activity to one single client with normal language keys.
These keys need to be in the format of standard AMXX keys:
  eg: ADMIN_KICK_1 = ADMIN: kick %s
      ADMIN_KICK_2 = ADMIN %s: kick %s
This depends on the amx_show_activity cvar.  See documentation for more details.
```
  
[colored_menus](https://amxx-bg.info/api/amxmisc/colored_menus) | ```
Returns if the mod running on the server supports colored menus.
```
  
[cstrike_running](https://amxx-bg.info/api/amxmisc/cstrike_running) | ```
Returns if the mod running on the server is a version of Counter-Strike.
```
  
[is_running](https://amxx-bg.info/api/amxmisc/is_running) | ```
Returns if the server is running a specific mod.
```
  
[get_basedir](https://amxx-bg.info/api/amxmisc/get_basedir) | ```
Retrieves the path to the AMXX base directory.
```
  
[get_configsdir](https://amxx-bg.info/api/amxmisc/get_configsdir) | ```
Retrieves the path to the AMXX configs directory.
```
  
[get_datadir](https://amxx-bg.info/api/amxmisc/get_datadir) | ```
Retrieves the path to the AMXX data directory.
```
  
[register_menu](https://amxx-bg.info/api/amxmisc/register_menu) | ```
Provides a shorthand to register a working menu.
```
  
[get_customdir](https://amxx-bg.info/api/amxmisc/get_customdir) | ```
Alias to get_configsdir provided for backwards compatibility. Originally
intended to retrieve the AMXX custom directory.
```
  
[AddMenuItem](https://amxx-bg.info/api/amxmisc/AddMenuItem) | ```
Adds a menu item/command to the admin menu (amxmodmenu) handled by the
"Menus Front-End" plugin, if it is loaded.
```
  
[AddClientMenuItem](https://amxx-bg.info/api/amxmisc/AddClientMenuItem) | ```
Adds a menu item/command to the client menu (amx_menu) handled by the
"Menus Front-End" plugin, if it is loaded. Items should be accessible by
non-admins.
```
  
[AddMenuItem_call](https://amxx-bg.info/api/amxmisc/AddMenuItem_call) | ```
Helper function used by AddMenuItem() and AddClientMenuItem()
```
  
[constraint_offset](https://amxx-bg.info/api/amxmisc/constraint_offset) | ```
Computes an offset from a given value while constraining it between the
specified bounds, rolling over if necessary.
```
  
[has_flag](https://amxx-bg.info/api/amxmisc/has_flag) | ```
Returns if the client has any of the specified admin flags.
```
  
[has_all_flags](https://amxx-bg.info/api/amxmisc/has_all_flags) | ```
Returns if the client has all of the specified admin flags.
```
  
[reset_menu](https://amxx-bg.info/api/amxmisc/reset_menu) | ```
Resets the client's menu.
```
  
[set_task_ex](https://amxx-bg.info/api/amxmisc/set_task_ex) | ```
Calls a function after a specified time has elapsed.
```
  
[get_players_ex](https://amxx-bg.info/api/amxmisc/get_players_ex) | ```
Stores a filtered list of client indexes to an array.
```
  
[get_playersnum_ex](https://amxx-bg.info/api/amxmisc/get_playersnum_ex) | ```
Returns the number of clients on the server that match the specified flags.
```
  

This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

