egister_concmd
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
register_concmd - Registers function which will be called from any console 
Syntax
register_concmd ( const cmd[],const function[],flags=-1, info[]="" ) 
Type
Native 
Notes
Example:   
`    
register_concmd("amx_mycommand","MyFunction",ADMIN_KICK,"Description of the command")   
  `   
  
A list of all the access list:   
ADMIN_RESERVATION   
ADMIN_IMMUNITY   
ADMIN_KICK   
ADMIN_BAN   
ADMIN_SLAY   
ADMIN_MAP   
ADMIN_CVAR   
ADMIN_CFG   
ADMIN_CHAT   
ADMIN_VOTE   
ADMIN_PASSWORD   
ADMIN_RCON   
ADMIN_LEVEL_A   
ADMIN_LEVEL_B   
ADMIN_LEVEL_C   
ADMIN_LEVEL_D   
ADMIN_LEVEL_E   
ADMIN_LEVEL_F   
ADMIN_LEVEL_G   
ADMIN_LEVEL_H   

