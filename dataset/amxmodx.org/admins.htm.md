. Configuration: Admins
The following instructions are for admins stored in addons\amxmodx\configs\users.ini. If you are using SQL, please refer to the SQL setion.  
  
Open users.ini with your favorite text editor. There are four parameters when adding a user:  
  
Authentication Style, Password, Access Rights, Connection Flags   
  
Generally, a users.ini entry will look like this:  
  
```
"STEAMID" "" "abcdefghijklmnopqrstu" "ce"
```
  
Or for a more concrete example:  
  
```
"STEAM_0:0:123456" "" "abcdefghijklmnopqrstu" "ce"
```
  
This means:  

  * Authentication: STEAM_0:0:123456
  * Password: None (auth by SteamID)
  * Access Rights: a through u
  * Connection Flags: SteamID + No Password

In general you should follow this example. Rarely should you ever need to authenticate by password + name, but it is possible. Here is what the entry would look like:  
  
```
"BAILOPAN" "mypass" "abcdefghijklmnopqrstu" "a"
```
  
Then to authenticate yourself, edit "autoexec.cfg" (or create it) in your client mod folder and add:  
  
```
setinfo "_pw" "mypass"
```
  
Where "_pw" is the setting for amx_password_field in amxx.cfg.  
  
The available access and connection flags are below.  
  

Important: Do not use "z" for admins.
  
Access Flag | Purpose  
---|---  
a | immunity (can't be kicked/baned/slayed/slaped and affected by other commmands)  
b | reservation (can join on reserved slots)  
c | amx_kick command  
d | amx_ban and amx_unban commands  
e | amx_slay and amx_slap commands  
f | amx_map command  
g | amx_cvar command (not all cvars will be available)  
h | amx_cfg command  
i | amx_chat and other chat commands  
j | amx_vote and other vote commands  
k | access to sv_password cvar (by amx_cvar command)  
l | access to amx_rcon command and rcon_password cvar (by amx_cvar command)  
m | custom level A (for additional plugins)  
n | custom level B  
o | custom level C  
p | custom level D  
q | custom level E  
r | custom level F  
s | custom level G  
t | custom level H  
u | menu access  
z | user (no admin)  
  
  
Connection Flag | Purpose  
---|---  
a | disconnect player on invalid password  
b | clan tag  
c | this is steamid/wonid  
d | this is ip  
e | password is not checked (only name/ip/steamid needed)
