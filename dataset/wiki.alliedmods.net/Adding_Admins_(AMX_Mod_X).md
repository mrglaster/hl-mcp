# Adding Admins (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#p-search)
## Contents
  * [1 Admins (non-SQL)](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Admins_.28non-SQL.29)
    * [1.1 Adding an Admin](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Adding_an_Admin)
    * [1.2 Removing an Admin](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Removing_an_Admin)
  * [2 Admins (SQL)](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Admins_.28SQL.29)
    * [2.1 Configuring Server](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Configuring_Server)
    * [2.2 Maintaining Admins](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Maintaining_Admins)
  * [3 Console Command](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Console_Command)
  * [4 Access Levels](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Access_Levels)
  * [5 Connection Flags](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Connection_Flags)


# Admins (non-SQL)
## Adding an Admin
First, open the amxmodx/configs/users.ini file with your favorite text editor. Scroll to the bottom. Admin entries are stored with four options: Authentication, Password, Access Right, Connection Properties. 
In the early days of [Half-Life 1](https://wiki.alliedmods.net/Half-Life_1 "Half-Life 1") it was common to have admins authenticate by name. However, now it is recommended to auth by steamid. An example of a typical admin entry is: 
```
"STEAM_0:0:123456" "" "abcdefghijklmnopqrstu" "ce"
```

Entries are one-per-line, and each of the four options are space separated, contained in double-quotes. This one means: 
  1. The user has [SteamID](https://wiki.alliedmods.net/index.php?title=SteamID&action=edit&redlink=1 "SteamID \(page does not exist\)") STEAM_0:0:123456
  2. The user has no password (steamid-authentication)
  3. Access rights are levels `a` through `u`
  4. The user is a steamid ("c") and has no password ("e")


It is also possible to authenticate by username: 
```
"BAILOPAN" "mypass" "abcdefghijklmnopqrstu" "a"
```

To authenticate, BAILOPAN would put this in his client's autoexec.cfg, where "_pw" is the value of "amx_password_field" in [amxx.cfg](https://wiki.alliedmods.net/Amxx.cfg "Amxx.cfg"). 
```
setinfo "_pw" "mypass"
```

For information on what access levels mean, see [Access Levels](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Access_Levels). 
`**Note:** It is important that you do not use the 'z' flag for admins because that's the non-admin flag.`
## Removing an Admin
Find the admin's entry in your amxmodx/configs/users.ini file, and put a semicolon in front of it. For example: 
```
;"STEAM_0:0:123456" "" "abcdefghijklmnopqrstu" "ce"
```

That will prevent the entry from being read. 
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/index.php?title=Ru:Adding_Admins_\(AMX_Mod_X\)&action=edit&redlink=1 "Ru:Adding Admins \(AMX Mod X\) \(page does not exist\)") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/Zh_cn:Adding_Admins_\(AMX_Mod_X\) "Zh cn:Adding Admins \(AMX Mod X\)") |   
# Admins (SQL)
AMX Mod X lets you store admin accounts in a MySQL database. This is ideal if you have multiple servers with common administrators. 
## Configuring Server
First, make sure you have configured your server for SQL by reading [Configuring AMX Mod X: SQL](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#SQL "Configuring AMX Mod X"). Then, enable the admin_sql.amxx plugin instead of admin.amxx, by opening amxmodx/configs/plugins.ini. You should change the first two entries to look something like this: 
```
;admin.amxx ; Disabled 
admin_sql.amxx ; SQL admins
```

## Maintaining Admins
Once the server loads for the first time, it will automatically create the table specified with `amx_sql_table`. 
You can either add an admin through an SQL tool like an SQL Console or phpMyAdmin, or you can add an admin [using amx_addadmin](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Console_Command "Adding Admins \(AMX Mod X\)"). 
If you choose to use SQL directly (or an interface), you must learn the table layout. There are four columns, each corresponding to one of the four properties listed above in [Adding an Admin](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\)#Adding_an_Admin). For example: 
```
INSERT INTO admins VALUES("STEAM_0:1:23456", "", "abcdefghijklmnopqrstu", "ce");
```

`**Note:** It is important that you do not use the 'z' flag for admins.`
For information on what access levels mean, see [AMX Mod X Access Levels](https://wiki.alliedmods.net/AMX_Mod_X_Access_Levels "AMX Mod X Access Levels"). 
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/index.php?title=Ru:Adding_Admins_\(AMX_Mod_X\)&action=edit&redlink=1 "Ru:Adding Admins \(AMX Mod X\) \(page does not exist\)") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/Zh_cn:Adding_Admins_\(AMX_Mod_X\) "Zh cn:Adding Admins \(AMX Mod X\)") |   
# Console Command
You can also use the console command amx_addadmin for adding admins. It will work for both [SQL](https://wiki.alliedmods.net/index.php?title=SQL&action=edit&redlink=1 "SQL \(page does not exist\)") and users.ini, depending on which plugin you have enabled. An example of using the command in-game: 
```
amx_addadmin "BAILOPAN" "abcdefghijklmnopqrstu"
```

Using the command from the server/[rcon](https://wiki.alliedmods.net/Rcon "Rcon") console: 
```
amx_addadmin "STEAM_0:1:23456" "abcdefghijklmnopqrstu"
```

# Access Levels
These access levels are the default access levels for the base [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X") plugins. 3rd party plugins may have different usages for them, although in general users try to stick to the intentions for each flag.       Access Flag  | Purpose   
---|---  
a  | immunity (can't be kicked/baned/slayed/slaped and affected by other commmands)   
b  | reservation (can join on reserved slots)   
c  | amx_kick command   
d  | amx_ban and amx_unban commands   
e  | amx_slay and amx_slap commands   
f  | amx_map command   
g  | amx_cvar command (not all cvars will be available)   
h  | amx_cfg command   
i  | amx_chat and other chat commands   
j  | amx_vote and other vote commands   
k  | access to sv_password cvar (by amx_cvar command)   
l  | access to amx_rcon command and rcon_password cvar (by amx_cvar command)   
m  | custom level A (for additional plugins)   
n  | custom level B   
o  | custom level C   
p  | custom level D   
q  | custom level E   
r  | custom level F   
s  | custom level G   
t  | custom level H   
u  | menu access   
z  | user (no admin)   
  

# Connection Flags
These flags control how [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X") attempts to authorize a connecting admin.       Connection Flag  | Purpose   
---|---  
a  | disconnect player on invalid password   
b  | clan tag   
c  | this is steamid/wonid   
d  | this is ip   
e  | password not checked (only name/ip/steamid needed)   
