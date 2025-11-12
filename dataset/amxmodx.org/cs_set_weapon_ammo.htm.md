s_set_weapon_ammo
[Cstrike](http://127.0.0.1:8000/content/index.htm) (cstrike.inc) 
Description
cs_set_weapon_ammo - Sets the amount of ammo in a player's weapon clip. 
Syntax
cs_set_weapon_ammo ( index, newammo ) 
Type
Native 
Notes
index is a player index from 1 to 32. 
User Contributed Notes
Freecode | Sep-25-04 13:14:59  
---|---  
The index in this instance is the index of the weapon not the person holding the weapon. So you must find the weapons index before using this native.   
  

