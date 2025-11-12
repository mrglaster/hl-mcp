. Configuration: Base CVARs
To edit these options, open "addons/amxmodx/configs/amxx.cfg" with your favorite text editor.   
  
CVAR | Default Setting | Purpose  
---|---|---  
amx_default_access | "z" | Sets the default access level for non-admin players.  
amx_password_field | "_pw" | Name of the setinfo key which a user should store their password in.  
amx_mode | 1 | Changes the mode of logging into a server:  
0 - Disable logging, players won't be checked and no access will be given.  
1 - Normal mode which obeys flags set in accounts.  
2 - Kick all players not on the users list.  
amx_show_activity | 2 | Sets the mode of admin activity on the server:  
0 - Disabled  
1 - Show action anonymously  
2 - Show action with the admin's name  
amx_scrollmsg | "Welcome to %hostname% -- This server is using AMX Mod X" 600 | Sets the parameters (message and frequency) for a scrolling message.  
amx_imessage | "Welcome to %hostname" "000255100"  
"This server is using AMX Mod X\nVisit http://www.amxmodx.org" "00010025" | Adds a center-typed colored message. The last parameter is in RRRGGGBBB format (red, green, blue).  
amx_freq_imessage | 180 | Frequency, in seconds, of the colored center messages.  
amx_flood_time | 0.75 | Chat flood prevention. Sets how fast a player can chat (in seconds).  
amx_reservation | 0 | Sets the amount of reserved slots.  
amx_time_display | "ab 1200" "ab 600" "ab 300" "ab 180" "ab 60" "bcde 11" | Sets flags for remaining time display:  
a - Display white text on bottom  
b - Use voice  
c - Don't add "remaining" in voice  
d - Don't add "hours/minutes/seconds" in voice  
e - Show/speak if current time is less than set in parameter  
amx_time_voice | 1 | Sets whether to announce "say thetime" and "say timeleft" with voice.  
amx_vote_delay | 10 | Sets the minimum delay in seconds between two voting sessions.  
amx_vote_time | 10 | Sets how long a voting sessions lasts for.  
amx_vote_answers | 1 | Displays who votes for which options, publically.  
amx_voteban_ratio | 0.40 | Ratio for a ban vote to be successful.  
amx_votekick_ratio | 0.40 | Ratio for a kick vote to be successful.  
amx_votemap_ratio | 0.40 | Ratio for a map vote to be successful.  
amx_vote_ratio | 0.02 | Ratio for a general vote to be successful.  
amx_extendmap_max | 90 | Maximum time a mapvote can be extended.  
amx_extendmap_step | 15 | Amount of time a map extensions adds.  
amx_client_languages | 1 | Enables or disables the ability for clients to choose their own language.  
amx_debug | 1 | Sets the debug mode for plugins:  
0 - No debugging (warning messages for plugin errors)  
1 - Plugins with "debug" option in plugins.ini are put into debug mode.  
2 - All plugins are put into debug mode (full backtraces for errors).  
Note that debug mode greatly decreases JIT performance.
