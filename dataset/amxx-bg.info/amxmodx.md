# Functions in amxmodx.inc
Function | Description  
---|---  
[plugin_init](https://amxx-bg.info/api/amxmodx/plugin_init) | ```
Called just after server activation.
```
  
[plugin_pause](https://amxx-bg.info/api/amxmodx/plugin_pause) | ```
Called just before the plugin is paused from execution.
```
  
[plugin_unpause](https://amxx-bg.info/api/amxmodx/plugin_unpause) | ```
Called just after the plugin is unpaused.
```
  
[server_changelevel](https://amxx-bg.info/api/amxmodx/server_changelevel) | ```
Called when the mod tries to change the map.
```
  
[plugin_cfg](https://amxx-bg.info/api/amxmodx/plugin_cfg) | ```
Called when all plugins went through plugin_init()
```
  
[plugin_end](https://amxx-bg.info/api/amxmodx/plugin_end) | ```
Called just before server deactivation and subsequent unloading of the
plugin.
```
  
[plugin_log](https://amxx-bg.info/api/amxmodx/plugin_log) | ```
Called when a message is about to be logged.
```
  
[plugin_precache](https://amxx-bg.info/api/amxmodx/plugin_precache) | ```
This forward allows plugins to add models, sounds and generic files to the
precache tables using the precache_* set of functions.
```
  
[client_infochanged](https://amxx-bg.info/api/amxmodx/client_infochanged) | ```
Called when a clients info has changed.
```
  
[client_connect](https://amxx-bg.info/api/amxmodx/client_connect) | ```
Called when a client is connecting.
```
  
[client_connectex](https://amxx-bg.info/api/amxmodx/client_connectex) | ```
Called when a client is connecting.
```
  
[client_authorized](https://amxx-bg.info/api/amxmodx/client_authorized) | ```
Called when the client gets a valid SteamID.
```
  
[client_disconnect](https://amxx-bg.info/api/amxmodx/client_disconnect) | ```
This function has no description.
```
  
[client_disconnected](https://amxx-bg.info/api/amxmodx/client_disconnected) | ```
Called when a client is disconnected from the server.
```
  
[client_remove](https://amxx-bg.info/api/amxmodx/client_remove) | ```
Called when a client entity has been removed from the server.
```
  
[client_command](https://amxx-bg.info/api/amxmodx/client_command) | ```
Called when a client attempts to execute a command.
```
  
[client_putinserver](https://amxx-bg.info/api/amxmodx/client_putinserver) | ```
Called when a client is entering the game.
```
  
[register_plugin](https://amxx-bg.info/api/amxmodx/register_plugin) | ```
Sets informations about the calling plugin.
```
  
[precache_model](https://amxx-bg.info/api/amxmodx/precache_model) | ```
Precaches a model file.
```
  
[precache_sound](https://amxx-bg.info/api/amxmodx/precache_sound) | ```
Precaches a sound file.
```
  
[precache_generic](https://amxx-bg.info/api/amxmodx/precache_generic) | ```
Precaches a generic file.
```
  
[precache_event](https://amxx-bg.info/api/amxmodx/precache_event) | ```
Precaches an event file.
```
  
[engine_changelevel](https://amxx-bg.info/api/amxmodx/engine_changelevel) | ```
Changes the map.
```
  
[set_user_info](https://amxx-bg.info/api/amxmodx/set_user_info) | ```
Sets info on the client.
```
  
[get_user_info](https://amxx-bg.info/api/amxmodx/get_user_info) | ```
Gets info from the client.
```
  
[set_localinfo](https://amxx-bg.info/api/amxmodx/set_localinfo) | ```
Sets info on the server.
```
  
[get_localinfo](https://amxx-bg.info/api/amxmodx/get_localinfo) | ```
Gets info from the server.
```
  
[show_motd](https://amxx-bg.info/api/amxmodx/show_motd) | ```
Shows text or a file in MOTD window.
```
  
[client_print](https://amxx-bg.info/api/amxmodx/client_print) | ```
Sends a message to the client.
```
  
[client_print_color](https://amxx-bg.info/api/amxmodx/client_print_color) | ```
Sends colored chat messages to clients.
```
  
[engclient_print](https://amxx-bg.info/api/amxmodx/engclient_print) | ```
Sends a message to the client via the engine.
```
  
[console_print](https://amxx-bg.info/api/amxmodx/console_print) | ```
Sends a message to the console of a client or the server.
```
  
[console_cmd](https://amxx-bg.info/api/amxmodx/console_cmd) | ```
Executes a command from the specified client or the server console.
```
  
[register_event](https://amxx-bg.info/api/amxmodx/register_event) | ```
Registers a function to be called on a given game event.
```
  
[register_event_ex](https://amxx-bg.info/api/amxmodx/register_event_ex) | ```
Registers a function to be called on a given game event.
```
  
[enable_event](https://amxx-bg.info/api/amxmodx/enable_event) | ```
Enables a function hook of a game event which has been previously registered with register_event_ex().
```
  
[disable_event](https://amxx-bg.info/api/amxmodx/disable_event) | ```
Disables a function hook of a game event which has been previously registered with register_event_ex().
```
  
[register_logevent](https://amxx-bg.info/api/amxmodx/register_logevent) | ```
Registers a function to be called on a given log event.
```
  
[enable_logevent](https://amxx-bg.info/api/amxmodx/enable_logevent) | ```
Enables a function hook of a game log event which has been previously registered with register_logevent().
```
  
[disable_logevent](https://amxx-bg.info/api/amxmodx/disable_logevent) | ```
Disables a function hook of a game log event which has been previously registered with register_logevent().
```
  
[set_hudmessage](https://amxx-bg.info/api/amxmodx/set_hudmessage) | ```
Sets display parameters for hudmessages.
```
  
[show_hudmessage](https://amxx-bg.info/api/amxmodx/show_hudmessage) | ```
Displays a message on the client HUD.
```
  
[set_dhudmessage](https://amxx-bg.info/api/amxmodx/set_dhudmessage) | ```
Sets display parameters for director hudmessages.
```
  
[show_dhudmessage](https://amxx-bg.info/api/amxmodx/show_dhudmessage) | ```
Displays a director message on the client HUD.
```
  
[show_menu](https://amxx-bg.info/api/amxmodx/show_menu) | ```
Displays a menu to the client.
```
  
[read_data](https://amxx-bg.info/api/amxmodx/read_data) | ```
Retrieves values from a client message.
```
  
[read_datanum](https://amxx-bg.info/api/amxmodx/read_datanum) | ```
Returns the number of values in the client message.
```
  
[read_datatype](https://amxx-bg.info/api/amxmodx/read_datatype) | ```
Returns the message id of the client message.
```
  
[read_logdata](https://amxx-bg.info/api/amxmodx/read_logdata) | ```
Retrieves current log message.
```
  
[read_logargc](https://amxx-bg.info/api/amxmodx/read_logargc) | ```
Returns number of log message arguments.
```
  
[read_logargv](https://amxx-bg.info/api/amxmodx/read_logargv) | ```
Retrieves argument of log message.
```
  
[parse_loguser](https://amxx-bg.info/api/amxmodx/parse_loguser) | ```
Parse log data about client.
```
  
[server_print](https://amxx-bg.info/api/amxmodx/server_print) | ```
Sends a message to the console of the server.
```
  
[is_map_valid](https://amxx-bg.info/api/amxmodx/is_map_valid) | ```
Returns if the given mapname is deemed valid by the engine.
```
  
[is_user_bot](https://amxx-bg.info/api/amxmodx/is_user_bot) | ```
Returns if the client is a bot.
```
  
[is_user_hltv](https://amxx-bg.info/api/amxmodx/is_user_hltv) | ```
Returns if the client is a HLTV proxy.
```
  
[is_user_authorized](https://amxx-bg.info/api/amxmodx/is_user_authorized) | ```
Returns if the client is authorized.
```
  
[is_user_connected](https://amxx-bg.info/api/amxmodx/is_user_connected) | ```
Returns if the client is connected.
```
  
[is_user_connecting](https://amxx-bg.info/api/amxmodx/is_user_connecting) | ```
Returns if the client is connecting.
```
  
[is_user_alive](https://amxx-bg.info/api/amxmodx/is_user_alive) | ```
Returns if the client is alive.
```
  
[is_dedicated_server](https://amxx-bg.info/api/amxmodx/is_dedicated_server) | ```
Returns if the server is a dedicated server.
```
  
[is_linux_server](https://amxx-bg.info/api/amxmodx/is_linux_server) | ```
Returns if the server is running on Linux.
```
  
[is_jit_enabled](https://amxx-bg.info/api/amxmodx/is_jit_enabled) | ```
Returns if the AMXX installation has the JIT enabled.
```
  
[get_amxx_verstring](https://amxx-bg.info/api/amxmodx/get_amxx_verstring) | ```
Retrieves the version string of the AMXX installation.
```
  
[get_user_attacker](https://amxx-bg.info/api/amxmodx/get_user_attacker) | ```
Returns the last known attacker of a client.
```
  
[get_user_aiming](https://amxx-bg.info/api/amxmodx/get_user_aiming) | ```
Traces the client's current aim vector to see if it hits something.
```
  
[get_user_frags](https://amxx-bg.info/api/amxmodx/get_user_frags) | ```
Returns the client's frags.
```
  
[get_user_armor](https://amxx-bg.info/api/amxmodx/get_user_armor) | ```
Returns the client's armor value.
```
  
[get_user_deaths](https://amxx-bg.info/api/amxmodx/get_user_deaths) | ```
Returns the client's death count.
```
  
[get_user_health](https://amxx-bg.info/api/amxmodx/get_user_health) | ```
Returns the client's health points.
```
  
[get_user_index](https://amxx-bg.info/api/amxmodx/get_user_index) | ```
Retrieves a client's index by name.
```
  
[get_user_ip](https://amxx-bg.info/api/amxmodx/get_user_ip) | ```
Retrieves the IP of a client or the server.
```
  
[user_has_weapon](https://amxx-bg.info/api/amxmodx/user_has_weapon) | ```
Returns if the client has the specified weapon in their inventory.
```
  
[get_user_weapon](https://amxx-bg.info/api/amxmodx/get_user_weapon) | ```
Returns weapon index of the currently carried weapon. Also allows retrieval
of ammo in the clip and backpack.
```
  
[get_user_ammo](https://amxx-bg.info/api/amxmodx/get_user_ammo) | ```
Retrieves ammo in the clip and backpack of the specified weapon.
```
  
[num_to_word](https://amxx-bg.info/api/amxmodx/num_to_word) | ```
Converts an integer to a text string.
```
  
[get_user_team](https://amxx-bg.info/api/amxmodx/get_user_team) | ```
Returns the team id of the client, and optionally retrieves the name of
the team.
```
  
[get_user_time](https://amxx-bg.info/api/amxmodx/get_user_time) | ```
Returns client's playing time in seconds.
```
  
[get_user_ping](https://amxx-bg.info/api/amxmodx/get_user_ping) | ```
Retrieves the ping and loss of a client.
```
  
[get_user_origin](https://amxx-bg.info/api/amxmodx/get_user_origin) | ```
Retrieves an origin related to the client.
```
  
[get_user_weapons](https://amxx-bg.info/api/amxmodx/get_user_weapons) | ```
Retrieves all weapons in the client inventory, stores them in an array, and
returns the inventory as a bitflag sum.
```
  
[get_weaponname](https://amxx-bg.info/api/amxmodx/get_weaponname) | ```
Retrieves the full name of a weapon.
```
  
[get_user_name](https://amxx-bg.info/api/amxmodx/get_user_name) | ```
Retrieves the name of a client or the server.
```
  
[get_user_authid](https://amxx-bg.info/api/amxmodx/get_user_authid) | ```
Retrieves the SteamID of a client.
```
  
[get_user_userid](https://amxx-bg.info/api/amxmodx/get_user_userid) | ```
Returns the userid of a client.
```
  
[user_slap](https://amxx-bg.info/api/amxmodx/user_slap) | ```
Slaps the client with specified power. Killing the client if applicable.
```
  
[user_kill](https://amxx-bg.info/api/amxmodx/user_kill) | ```
Kills a client.
```
  
[log_amx](https://amxx-bg.info/api/amxmodx/log_amx) | ```
Logs a message to the current AMXX log file.
```
  
[log_message](https://amxx-bg.info/api/amxmodx/log_message) | ```
Logs a message to the current server log file.
```
  
[elog_message](https://amxx-bg.info/api/amxmodx/elog_message) | ```
Logs a message hookable by plugins to the current server log file.
```
  
[log_to_file](https://amxx-bg.info/api/amxmodx/log_to_file) | ```
Logs a message to the specified file
```
  
[get_playersnum](https://amxx-bg.info/api/amxmodx/get_playersnum) | ```
Returns the number of clients on the server.
```
  
[get_players](https://amxx-bg.info/api/amxmodx/get_players) | ```
Stores a filtered list of client indexes to an array.
```
  
[read_argv](https://amxx-bg.info/api/amxmodx/read_argv) | ```
Retrieves argument of client command as string.
```
  
[read_argv_int](https://amxx-bg.info/api/amxmodx/read_argv_int) | ```
Retrieves argument of client command as integer value.
```
  
[read_argv_float](https://amxx-bg.info/api/amxmodx/read_argv_float) | ```
Retrieves argument of client command as float value.
```
  
[read_args](https://amxx-bg.info/api/amxmodx/read_args) | ```
Retrieves full client command string.
```
  
[read_argc](https://amxx-bg.info/api/amxmodx/read_argc) | ```
Returns number of client command arguments.
```
  
[read_flags](https://amxx-bg.info/api/amxmodx/read_flags) | ```
Converts a flag string to a bitflag value.
```
  
[get_flags](https://amxx-bg.info/api/amxmodx/get_flags) | ```
Converts a bitflag value to a flag string.
```
  
[find_player](https://amxx-bg.info/api/amxmodx/find_player) | ```
Find a player given a filter.
```
  
[find_player_ex](https://amxx-bg.info/api/amxmodx/find_player_ex) | ```
Find a player given a filter.
```
  
[remove_quotes](https://amxx-bg.info/api/amxmodx/remove_quotes) | ```
Removes double-quotes from the beginning and end of a string.
```
  
[client_cmd](https://amxx-bg.info/api/amxmodx/client_cmd) | ```
Executes a command on the client.
```
  
[engclient_cmd](https://amxx-bg.info/api/amxmodx/engclient_cmd) | ```
Execute a command from the client without actually sending it to the client's
DLL.
```
  
[amxclient_cmd](https://amxx-bg.info/api/amxmodx/amxclient_cmd) | ```
Execute a command from the client without actually sending it to the client's
DLL. This triggers plugin command hooks.
```
  
[server_cmd](https://amxx-bg.info/api/amxmodx/server_cmd) | ```
Queues a command to be executed from the server console.
```
  
[get_mapname](https://amxx-bg.info/api/amxmodx/get_mapname) | ```
Retrieves the name of the currently played map.
```
  
[get_timeleft](https://amxx-bg.info/api/amxmodx/get_timeleft) | ```
Returns time remaining on map.
```
  
[get_gametime](https://amxx-bg.info/api/amxmodx/get_gametime) | ```
Returns the game time based on the game tick.
```
  
[get_maxplayers](https://amxx-bg.info/api/amxmodx/get_maxplayers) | ```
Returns the maxplayers setting of the current server, that is how many
clients it supports.
```
  
[get_modname](https://amxx-bg.info/api/amxmodx/get_modname) | ```
Retrieves the name of the currently played mod.
```
  
[get_time](https://amxx-bg.info/api/amxmodx/get_time) | ```
Retrieves the current time using the specified format string.
```
  
[format_time](https://amxx-bg.info/api/amxmodx/format_time) | ```
Retrieves the provided time using the specified format string.
```
  
[get_systime](https://amxx-bg.info/api/amxmodx/get_systime) | ```
Returns the system time as a unix timestamp (number of seconds since unix
epoch).
```
  
[parse_time](https://amxx-bg.info/api/amxmodx/parse_time) | ```
Converts time strings to unix time stamp.
```
  
[set_task](https://amxx-bg.info/api/amxmodx/set_task) | ```
Calls a function after a specified time has elapsed.
```
  
[remove_task](https://amxx-bg.info/api/amxmodx/remove_task) | ```
Removes all tasks with the specified id.
```
  
[change_task](https://amxx-bg.info/api/amxmodx/change_task) | ```
Modifies the time interval of all tasks with the specified id.
```
  
[task_exists](https://amxx-bg.info/api/amxmodx/task_exists) | ```
Returns if a task with the specified id exists.
```
  
[set_user_flags](https://amxx-bg.info/api/amxmodx/set_user_flags) | ```
Sets the specified admin flags to a client.
```
  
[get_user_flags](https://amxx-bg.info/api/amxmodx/get_user_flags) | ```
Returns the client's admin flags as a bitflag sum.
```
  
[remove_user_flags](https://amxx-bg.info/api/amxmodx/remove_user_flags) | ```
Removes the specified admin flags from a client.
```
  
[register_clcmd](https://amxx-bg.info/api/amxmodx/register_clcmd) | ```
Registers a callback to be called when the client executes a command from the
console.
```
  
[register_concmd](https://amxx-bg.info/api/amxmodx/register_concmd) | ```
Registers a callback to be called when the client or server executes a
command from the console.
```
  
[register_srvcmd](https://amxx-bg.info/api/amxmodx/register_srvcmd) | ```
Registers a callback to be called when the server executes a command from the
console.
```
  
[get_clcmd](https://amxx-bg.info/api/amxmodx/get_clcmd) | ```
Retrieves information about a client command.
```
  
[get_clcmdsnum](https://amxx-bg.info/api/amxmodx/get_clcmdsnum) | ```
Returns number of registered client commands.
```
  
[get_srvcmd](https://amxx-bg.info/api/amxmodx/get_srvcmd) | ```
Retrieves information about a server command.
```
  
[get_srvcmdsnum](https://amxx-bg.info/api/amxmodx/get_srvcmdsnum) | ```
Returns number of registered server commands.
```
  
[get_concmd](https://amxx-bg.info/api/amxmodx/get_concmd) | ```
Retrieves information about a console command.
```
  
[get_concmd_plid](https://amxx-bg.info/api/amxmodx/get_concmd_plid) | ```
Returns the parent plugin id of a console command.
```
  
[get_concmdsnum](https://amxx-bg.info/api/amxmodx/get_concmdsnum) | ```
Returns number of registered console commands.
```
  
[register_menuid](https://amxx-bg.info/api/amxmodx/register_menuid) | ```
Returns unique menu id of a menu.
```
  
[register_menucmd](https://amxx-bg.info/api/amxmodx/register_menucmd) | ```
Registers a callback function to a menu id and keys.
```
  
[get_user_menu](https://amxx-bg.info/api/amxmodx/get_user_menu) | ```
Returns if the client is watching a menu.
```
  
[server_exec](https://amxx-bg.info/api/amxmodx/server_exec) | ```
Forces the server to execute the command queue immediately.
```
  
[emit_sound](https://amxx-bg.info/api/amxmodx/emit_sound) | ```
Emits a sound from an entity from the engine.
```
  
[random_float](https://amxx-bg.info/api/amxmodx/random_float) | ```
Returns a random floating point value generated by the engine.
```
  
[random_num](https://amxx-bg.info/api/amxmodx/random_num) | ```
Returns a random integer value generated by the engine.
```
  
[get_user_msgid](https://amxx-bg.info/api/amxmodx/get_user_msgid) | ```
Returns unique id of a client message.
```
  
[get_user_msgname](https://amxx-bg.info/api/amxmodx/get_user_msgname) | ```
Retrieves the client message name from a message id.
```
  
[get_xvar_id](https://amxx-bg.info/api/amxmodx/get_xvar_id) | ```
Returns a unique id for a public variable.
```
  
[xvar_exists](https://amxx-bg.info/api/amxmodx/xvar_exists) | ```
Returns if a public variable exists in any loaded plugin.
```
  
[get_xvar_num](https://amxx-bg.info/api/amxmodx/get_xvar_num) | ```
Returns the integer value of a public variable.
```
  
[get_xvar_float](https://amxx-bg.info/api/amxmodx/get_xvar_float) | ```
Returns the float value of a public variable.
```
  
[set_xvar_num](https://amxx-bg.info/api/amxmodx/set_xvar_num) | ```
Sets the integer value of a public variable.
```
  
[set_xvar_float](https://amxx-bg.info/api/amxmodx/set_xvar_float) | ```
Sets the float value of a public variable.
```
  
[is_module_loaded](https://amxx-bg.info/api/amxmodx/is_module_loaded) | ```
Returns if a module is loaded.
```
  
[get_module](https://amxx-bg.info/api/amxmodx/get_module) | ```
Retrieves info about a module by module index.
```
  
[get_modulesnum](https://amxx-bg.info/api/amxmodx/get_modulesnum) | ```
Returns the number of currently registered modules.
```
  
[is_plugin_loaded](https://amxx-bg.info/api/amxmodx/is_plugin_loaded) | ```
Returns if a plugin is loaded by registered name or filename.
```
  
[get_plugin](https://amxx-bg.info/api/amxmodx/get_plugin) | ```
Retrieves info about a plugin by plugin index.
```
  
[get_pluginsnum](https://amxx-bg.info/api/amxmodx/get_pluginsnum) | ```
Returns the number of loaded AMXX plugins.
```
  
[pause](https://amxx-bg.info/api/amxmodx/pause) | ```
Pauses a plugin so it will not be executed until it is unpaused.
```
  
[unpause](https://amxx-bg.info/api/amxmodx/unpause) | ```
Unpauses a plugin so it will resume execution if it was previously paused.
```
  
[callfunc_begin](https://amxx-bg.info/api/amxmodx/callfunc_begin) | ```
Initiates a function call to this or another plugin by function name.
```
  
[callfunc_begin_i](https://amxx-bg.info/api/amxmodx/callfunc_begin_i) | ```
Initiates a function call to this or another plugin by function id.
```
  
[get_func_id](https://amxx-bg.info/api/amxmodx/get_func_id) | ```
Retrieves a functions id for use with callfunc_begin_i()
```
  
[callfunc_push_int](https://amxx-bg.info/api/amxmodx/callfunc_push_int) | ```
Pushes an int value onto the current call.
```
  
[callfunc_push_float](https://amxx-bg.info/api/amxmodx/callfunc_push_float) | ```
Pushes a float value onto the current call.
```
  
[callfunc_push_intrf](https://amxx-bg.info/api/amxmodx/callfunc_push_intrf) | ```
Pushes an int value reference onto the current call.
```
  
[callfunc_push_floatrf](https://amxx-bg.info/api/amxmodx/callfunc_push_floatrf) | ```
Pushes a float value reference onto the current call.
```
  
[callfunc_push_str](https://amxx-bg.info/api/amxmodx/callfunc_push_str) | ```
Pushes a string onto the current call.
```
  
[callfunc_push_array](https://amxx-bg.info/api/amxmodx/callfunc_push_array) | ```
Pushes an array onto the current call.
```
  
[callfunc_end](https://amxx-bg.info/api/amxmodx/callfunc_end) | ```
Completes the call to a function.
```
  
[inconsistent_file](https://amxx-bg.info/api/amxmodx/inconsistent_file) | ```
Called when an inconsistent file is encountered by the engine.
```
  
[force_unmodified](https://amxx-bg.info/api/amxmodx/force_unmodified) | ```
Forces the clients and server to be running with the same version of a
specified file.
```
  
[md5](https://amxx-bg.info/api/amxmodx/md5) | ```
Calculates the MD5 keysum of a string.
```
  
[md5_file](https://amxx-bg.info/api/amxmodx/md5_file) | ```
Calculates the MD5 keysum of a file.
```
  
[hash_string](https://amxx-bg.info/api/amxmodx/hash_string) | ```
Generate a hash value (message digest)
```
  
[hash_file](https://amxx-bg.info/api/amxmodx/hash_file) | ```
Generate a hash value using the contents of a given file
```
  
[plugin_flags](https://amxx-bg.info/api/amxmodx/plugin_flags) | ```
Returns the internal flags set on the plugin's state.
```
  
[plugin_modules](https://amxx-bg.info/api/amxmodx/plugin_modules) | ```
Allows plugins to declare module dependencies using require_module()
```
  
[require_module](https://amxx-bg.info/api/amxmodx/require_module) | ```
Adds a module dependency.
```
  
[is_amd64_server](https://amxx-bg.info/api/amxmodx/is_amd64_server) | ```
Returns if the server is 64 bit.
```
  
[find_plugin_byfile](https://amxx-bg.info/api/amxmodx/find_plugin_byfile) | ```
Returns plugin id by filename.
```
  
[plugin_natives](https://amxx-bg.info/api/amxmodx/plugin_natives) | ```
Called before plugin_init(), allows the plugin to register natives.
```
  
[register_native](https://amxx-bg.info/api/amxmodx/register_native) | ```
Registers a native.
```
  
[register_library](https://amxx-bg.info/api/amxmodx/register_library) | ```
Registers the plugin as a library.
```
  
[log_error](https://amxx-bg.info/api/amxmodx/log_error) | ```
Logs an error in the native and breaks into the AMXX debugger.
```
  
[param_convert](https://amxx-bg.info/api/amxmodx/param_convert) | ```
Converts a parameter to work as a by-reference parameter.
```
  
[get_string](https://amxx-bg.info/api/amxmodx/get_string) | ```
Retrieves a string from the plugin calling the native.
```
  
[set_string](https://amxx-bg.info/api/amxmodx/set_string) | ```
Copies a string to the plugin calling the native.
```
  
[get_param](https://amxx-bg.info/api/amxmodx/get_param) | ```
Returns the integer value of a parameter from the plugin calling the native.
```
  
[get_param_f](https://amxx-bg.info/api/amxmodx/get_param_f) | ```
Returns the float value of a parameter from the plugin calling the native.
```
  
[get_param_byref](https://amxx-bg.info/api/amxmodx/get_param_byref) | ```
Returns the integer value of a by-reference parameter from the plugin calling
the native.
```
  
[get_float_byref](https://amxx-bg.info/api/amxmodx/get_float_byref) | ```
Returns the float value of a by-reference parameter from the plugin calling
the native.
```
  
[set_param_byref](https://amxx-bg.info/api/amxmodx/set_param_byref) | ```
Sets the integer value of a by-reference parameter to the plugin calling the
native.
```
  
[set_float_byref](https://amxx-bg.info/api/amxmodx/set_float_byref) | ```
Sets the float value of a by-reference parameter to the plugin calling the
native.
```
  
[get_array](https://amxx-bg.info/api/amxmodx/get_array) | ```
Retrieves an array from the plugin calling the native.
```
  
[get_array_f](https://amxx-bg.info/api/amxmodx/get_array_f) | ```
Retrieves a float array from the plugin calling the native.
```
  
[set_array](https://amxx-bg.info/api/amxmodx/set_array) | ```
Copies an array to the plugin calling the native.
```
  
[set_array_f](https://amxx-bg.info/api/amxmodx/set_array_f) | ```
Copies a float array to the plugin calling the native.
```
  
[set_error_filter](https://amxx-bg.info/api/amxmodx/set_error_filter) | ```
Allows to trap error messages that occur in a plugin.
```
  
[dbg_trace_begin](https://amxx-bg.info/api/amxmodx/dbg_trace_begin) | ```
Returns a trace handle for the item at the top of the traced call stack.
```
  
[dbg_trace_next](https://amxx-bg.info/api/amxmodx/dbg_trace_next) | ```
Returns the next item in a traced call stack.
```
  
[dbg_trace_info](https://amxx-bg.info/api/amxmodx/dbg_trace_info) | ```
Retrieves the call stack info for a trace.
```
  
[dbg_fmt_error](https://amxx-bg.info/api/amxmodx/dbg_fmt_error) | ```
Retrieves the formatted error string from a trace.
```
  
[set_native_filter](https://amxx-bg.info/api/amxmodx/set_native_filter) | ```
Sets a native filter, letting the plugin intercept and handle an
automatic native requirement.
```
  
[set_module_filter](https://amxx-bg.info/api/amxmodx/set_module_filter) | ```
Sets a module/library filter, letting the plugin intercept and handle an
automatic module requirement.
```
  
[abort](https://amxx-bg.info/api/amxmodx/abort) | ```
Aborts execution of the current callback by throwing an error.
```
  
[module_exists](https://amxx-bg.info/api/amxmodx/module_exists) | ```
Returns if a specific module is loaded.
```
  
[LibraryExists](https://amxx-bg.info/api/amxmodx/LibraryExists) | ```
Returns if a specific library or class is loaded.
```
  
[next_hudchannel](https://amxx-bg.info/api/amxmodx/next_hudchannel) | ```
Returns the next valid hudchannel for the client.
```
  
[CreateHudSyncObj](https://amxx-bg.info/api/amxmodx/CreateHudSyncObj) | ```
Creates a HUD synchronization object.
```
  
[ShowSyncHudMsg](https://amxx-bg.info/api/amxmodx/ShowSyncHudMsg) | ```
Displays a synchronized HUD message.
```
  
[ClearSyncHud](https://amxx-bg.info/api/amxmodx/ClearSyncHud) | ```
Clears the display on a HUD sync object.
```
  
[int3](https://amxx-bg.info/api/amxmodx/int3) | ```
Triggers the software interrupt 3, used for breaking into an attached
debugger.
```
  
[set_fail_state](https://amxx-bg.info/api/amxmodx/set_fail_state) | ```
Sets the calling plugin to a failed state.
```
  
[get_var_addr](https://amxx-bg.info/api/amxmodx/get_var_addr) | ```
Returns the reference address of the variable passed in.
```
  
[get_addr_val](https://amxx-bg.info/api/amxmodx/get_addr_val) | ```
Returns the value of an address.
```
  
[set_addr_val](https://amxx-bg.info/api/amxmodx/set_addr_val) | ```
Sets the value of an address.
```
  
[CreateMultiForward](https://amxx-bg.info/api/amxmodx/CreateMultiForward) | ```
Creates a global forward that will be called in all plugins.
```
  
[CreateOneForward](https://amxx-bg.info/api/amxmodx/CreateOneForward) | ```
Creates a private forward that will be called in a single plugin.
```
  
[PrepareArray](https://amxx-bg.info/api/amxmodx/PrepareArray) | ```
Prepares an array for use in a forward. Pass the result ExecuteForward()
instead of the array itself.
```
  
[ExecuteForward](https://amxx-bg.info/api/amxmodx/ExecuteForward) | ```
Executes a forward.
```
  
[DestroyForward](https://amxx-bg.info/api/amxmodx/DestroyForward) | ```
Destroys and deallocates a forward.
```
  
[arrayset](https://amxx-bg.info/api/amxmodx/arrayset) | ```
Sets all elements of array to a specified value.
```
  
[get_weaponid](https://amxx-bg.info/api/amxmodx/get_weaponid) | ```
Returns the weapon id associated with a weapon name.
```
  
[admins_push](https://amxx-bg.info/api/amxmodx/admins_push) | ```
Adds an admin to the dynamic admin storage for lookup at a later time.
```
  
[admins_num](https://amxx-bg.info/api/amxmodx/admins_num) | ```
Returns the number of admins in the dynamic admin storage.
```
  
[admins_lookup](https://amxx-bg.info/api/amxmodx/admins_lookup) | ```
Retrieves information about a dynamically stored admin.
```
  
[admins_flush](https://amxx-bg.info/api/amxmodx/admins_flush) | ```
Clears the list of dynamically stored admins.
```
  
[has_map_ent_class](https://amxx-bg.info/api/amxmodx/has_map_ent_class) | ```
Returns if a map contains at least one entity with the provided class name.
```
  
[OnConfigsExecuted](https://amxx-bg.info/api/amxmodx/OnConfigsExecuted) | ```
Called when the map has loaded, and all configs are done executing.
This includes servercfgfile (server.cfg), amxx.cfg, plugin's config, and
per-map config.
```
  
[OnAutoConfigsBuffered](https://amxx-bg.info/api/amxmodx/OnAutoConfigsBuffered) | ```
Called when the map has loaded, right after plugin_cfg() but any time
before OnConfigsExecuted.  It's called after amxx.cfg and  all
AutoExecConfig() exec commands have been added to the server command buffer.
```
  
[AutoExecConfig](https://amxx-bg.info/api/amxmodx/AutoExecConfig) | ```
Specifies that the given config file should be executed after plugin load.
```
  
[RequestFrame](https://amxx-bg.info/api/amxmodx/RequestFrame) | ```
Creates a single use hook for the next frame.
```
  

This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

