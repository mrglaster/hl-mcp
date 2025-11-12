. Commands
  

Content:
  * [Admin Commands](http://127.0.0.1:8000/content/cmds.htm#admin)
  * [Chat Commands](http://127.0.0.1:8000/content/cmds.htm#chat)
  * [Vote Commands](http://127.0.0.1:8000/content/cmds.htm#vote)
  * [Stats Commands](http://127.0.0.1:8000/content/cmds.htm#stats)
  * [Say Commands](http://127.0.0.1:8000/content/cmds.htm#say)
  * [Menu Commands](http://127.0.0.1:8000/content/cmds.htm#menu)
  * [Config Commands](http://127.0.0.1:8000/content/cmds.htm#cfgs)
  * [RCON Commands](http://127.0.0.1:8000/content/cmds.htm#rcon)

Console commands are entered into the console like this:  
  
```
amx_<command> <option1> <option2> [option3]
```
  
Required options are shown with <>, optional parameters are shown with []. Do not actually type <> or [].   
  
To view in-game command help, use this in the console:   
  
```
amx_help
```
  
**Admin Commands** Command | Format | Access | Description  
---|---|---|---  
amx_kick | <name or #userid> [reason] | ADMIN_KICK | Kicks a player.  
amx_ban | <name or #userid> <time> [reason] | ADMIN_BAN | Bans a player.  
amx_addban | <authid or ip> <minutes> [reason] | ADMIN_BAN | Adds a ban to the server banlist.  
amx_unban | <authid or ip> | ADMIN_BAN | Unbans a player.  
amx_slay | <name or #userid> | ADMIN_SLAY | Slays a player.  
amx_slap | <name or #userid> [damage] | ADMIN_SLAY | Slaps a player for variable damage.  
amx_leave | <tag> [tag1] [tag2] [tag3] | ADMIN_KICK | Kicks all players not wearing one of the tags.  
amx_pause |  | ADMIN_CVAR | Pauses or unpauses the game.  
amx_who |  | ADMIN_ADMIN | Displays who is on the server.  
amx_cvar | <cvar> [value] | ADMIN_CVAR | Changes or displays a cvar value.  
amx_map | <mapname> | ADMIN_MAP | Changes map.  
amx_cfg | <filename> | ADMIN_CFG | Executes a server-side config file.  
amx_rcon | <rcon command line> | ADMIN_RCON | Executes a command on the server console.  
amx_plugins |  | ADMIN_ADMIN | Lists all loaded plugins.  
amx_modules |  | ADMIN_ADMIN | Lists all loaded modules.  
  
**Chat Commands** Command | Format | Access | Description  
---|---|---|---  
amx_say | <message> | ADMIN_CHAT | Sends a message to all players through normal say.  
amx_chat | <message> | ADMIN_CHAT | Sends a message to all admins through normal chat.  
amx_psay | <name or #userid> <message> | ADMIN_CHAT | Sends a private message to a player.  
amx_tsay | <color> <message> | ADMIN_CHAT | Sends a left side HUD message to all players.  
amx_csay | <color> <message> | ADMIN_CHAT | Sends a center HUD message to all players.  
  
**Vote Commands** Command | Format | Access | Description  
---|---|---|---  
amx_votemap | <map> [map] [map] [map] | ADMIN_VOTE | Starts a vote for a map.  
amx_votekick | <name or #userid> | ADMIN_VOTE | Starts a vote to kick a player.  
amx_voteban | <name or #userid> | ADMIN_VOTE | Starts a vote to ban a player.  
amx_vote | <question> <answer1> <answer2> | ADMIN_VOTE | Starts a custom poll.  
amx_cancelvote |  | ADMIN_VOTE | Cancels the last poll in progress.  
  
**Stats Commands** Command | Format | Access | Description  
---|---|---|---  
say /hp |  |  | Displays information about your killer.  
say /statsme |  |  | Displays your stats.  
say /stats |  |  | Displays other players' stats.  
say /top15 |  |  | Displays the top 15 players.  
say /rank |  |  | Displays your rank on the server.  
  
**Say Commands** Command | Format | Access | Description  
---|---|---|---  
say nextmap |  |  | Displays the next map in the mapcycle.  
say timeleft |  |  | Displays the time left in the map.  
say thetime |  |  | Displays the current time.  
  
**Menu Commands** Command | Format | Access | Description  
---|---|---|---  
amxmodmenu |  | ADMIN_MENU | Displays the main AMX Mod X menu.  
amx_cvarmenu |  | ADMIN_CVAR | Displays the CVAR menu.  
amx_mapmenu |  | ADMIN_MAP | Displays the map change menu.  
amx_votemapmenu |  | ADMIN_MAP | Displays the map voting menu.  
amx_kickmenu |  | ADMIN_KICK | Displays kick menu.  
amx_banmenu |  | ADMIN_BAN | Displays ban menu.  
amx_slapmenu |  | ADMIN_SLAY | Displays slap/slay menu.  
amx_teammenu |  | ADMIN_LEVEL_A | Displays team switch menu.  
amx_clcmdmenu |  | ADMIN_LEVEL_A | Displays client commands menu.  
amx_restmenu |  | ADMIN_CFG | Displays weapon restriction menu.  
amx_teleportmenu |  | ADMIN_CFG | Displays teleport menu.  
amx_pausecfgmenu |  | ADMIN_CFG | Pause/unpause plugins with menu.  
amx_statscfgmenu |  | ADMIN_CFG | Displays stats configuration menu.  
  
**Config Commands** Command: | amx_pausecfg  
---|---  
Format: | <command> [name]  
Access: | ADMIN_CFG  
Description: | Command list available:  
off - Pauses all plugins not in the list.  
on - Unpauses all plugins.  
stop <file> - Stops a plugin.  
pause <file> - Pauses a plugin.  
enable <file> - Enables a plugin.  
save - Saves a list of stopped plugins.  
clear - Clears a list of stopped plugins.  
list [id] - Lists plugins.  
add <title> - Marks a plugin as unpauseable.   
  
Command: | amx_statscfg  
---|---  
Format: | <command> [parameters]  
Access: | ADMIN_CFG  
Description: | Command list available:  
on <variable> - Enable specific option.  
off <variable> - Disable specific option.  
save - Save stats configuration.  
load - Load stats configuration.  
list [id] - List stats statuses.  
add <name> <variable> - Add stat variable to the list.   
  
**RCON Commands** Command: | amxx  
---|---  
Format: | <command> [parameters]  
Access: |   
Description: | Command list available:  
amxx version - Display version.  
amxx modules - Display modules.  
amxx plugins - Display plugins.  
amxx gpl - Display the GNU General Public License  
amxx cvars - Display AMX Mod X registered CVARs.  
amxx cmds - Display AMX Mod X registered commands.  
amxx pause - Pause a running plugin.  
amxx unpause - Unpause a running plugin.the list. 
