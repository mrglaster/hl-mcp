s_get_user_bpammo
[Cstrike](http://127.0.0.1:8000/content/index.htm) (cstrike.inc) 
Description
cs_get_user_bpammo - Returns the amount of ammo in a player's backpack for a specific weapon. 
Syntax
cs_get_user_bpammo ( index, weapon ) 
Type
Native 
Notes
index is a player index from 1 to 32. weapon is a weapon index (see amxconst.inc for CS weapon definitions).   
  
Some weapons share ammo types. Below is a list of weapons, ones on the same line do this.   
* awm   
* scout, ak, g3   
* para   
* famas, m4a1, aug, sg550, galil, sg552   
* m3, xm   
* usp, ump, mac   
* fiveseven, p90   
* deagle   
* p228   
* glock, mp5, tmp, elites   
* flash   
* he   
* smoke
