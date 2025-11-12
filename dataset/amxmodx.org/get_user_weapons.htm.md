et_user_weapons
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_weapons - Returns a list of all the carried weapons of a player. 
Syntax
get_user_weapons ( index, weapons[32], &num ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
The weapons array passed as the second parameter is filled with a list of weapon indices, from 0 to num-1. num will be filled with the number of weapons found (passed byref).   
  
Example:`    
new Weapons[32]   
new numWeapons, i, weapon   
get_user_weapons(id, Weapons, numWeapons)   
for (i=0; i<numWeapns; i++)   
  
   weapon = Weapons[i]   
}  `
User Contributed Notes
slayerized at gmail dot com | Jul-15-05 12:35:48  
---|---  
` new Weapons[32]   
new numWeapons, i, weapon   
get_user_weapons(id, Weapons, numWeapons)   
for (i=0; i<numWeapons; i++)   
{   
   weapon = Weapons[i]   
}  ` Just fixing a little typo in the example.   
  

