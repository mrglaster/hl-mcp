et_user_authid
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_authid - Finds the authentication id of a player. 
Syntax
get_user_authid ( index, authid[], len ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
Stores the authid for a maximum length of len characters.   
  
On WON, this is the WONID. On Steam, it is the SteamID. WONIDs are large integers, SteamIDs look like: STEAM_0:x:yyyyyy.   
The max lenght of a STEAM`id is 34 bytes.
