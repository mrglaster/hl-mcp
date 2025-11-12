ser_has_weapon
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
user_has_weapon - Returns if a player has the weapon or not. 
Syntax
user_has_weapon ( index, weapon, [ setweapon ] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
weapon is an index into the player's weapon bitfield. If setweapon is used, you can toggle whether the bit is set or not.   
  
Note: Will not work right on all modifications. Check the mod's custom module for a mod-specific function.
