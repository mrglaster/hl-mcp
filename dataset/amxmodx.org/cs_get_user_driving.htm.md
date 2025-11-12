s_get_user_driving
[Cstrike](http://127.0.0.1:8000/content/index.htm) (cstrike.inc) 
Description
cs_get_user_driving - Returns different values depending on if user is driving a vehicle. 
Syntax
cs_get_user_driving ( index ) 
Type
Native 
Notes
Return values:   
0: no driving   
1: driving, but standing still   
2-4: driving, different positive speeds   
5: driving, negative speed (backing)   
  
Note: these values were tested quickly, they may differ.
