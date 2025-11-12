egister_cvar
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
register_cvar - Registers new cvar for HL engine. 
Syntax
register_cvar ( const name[],const string[],flags = 0,Float:fvalue = 0.0 ) 
Type
Native 
Notes
Example:   
`    
register_cvar("amx_MyCvar","1",FCVAR_SERVER|FCVAR_EXTDLL|FCVAR_UNLOGGED|FCVAR_SPONLY)   
  `   
FCVAR_ARCHIVE set to cause it to be saved to vars.rc   
FCVAR_USERINFO changes the client's info string   
FCVAR_SERVER notifies players when changed   
FCVAR_EXTDLL defined by external DLL   
FCVAR_CLIENTDLL defined by the client dll   
FCVAR_PROTECTED It's a server cvar, but we don't send the data since it's a password, etc. Sends 1 if it's not bland/zero, 0 otherwise as value   
FCVAR_SPONLY This cvar cannot be changed by clients connected to a multiplayer server.   
FCVAR_PRINTABLEONLY This cvar's string cannot contain unprintable characters ( e.g., used for player name etc ).   
FCVAR_UNLOGGED If this is a FCVAR_SERVER, don't log changes to the log file / console if we are creating a log
