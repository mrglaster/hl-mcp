et_user_info
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
set_user_info - Sets an info value on a player 
Syntax
set_user_info ( index, const info[], const value[] ) 
Type
Native 
Notes
index is a player index from 1 to 32. 
User Contributed Notes
rh at pdc dot ru | Oct-10-04 14:26:18  
---|---  
Such a simple function but still full of surprises! Do not try to set info on user id 0 (which is server itself) otherwise you'll end up with nasty runtime error. You may want to use [set_localinfo](http://127.0.0.1:8000/content/funcwiki.php?go=func&id=19) instead.   
  
rh at pdc dot ru | Aug-18-04 17:05:01  
---|---  
This function does not seem to save info to client's config. Had to execute ` client_cmd(index, "setinfo %s %s", info, value)  ` instead...   
  

