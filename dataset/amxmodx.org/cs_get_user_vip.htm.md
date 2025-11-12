s_get_user_vip
[Cstrike](http://127.0.0.1:8000/content/index.htm) (cstrike.inc) 
Description
cs_get_user_vip - Returns 1 if the player is the VIP, 0 otherwise. 
Syntax
cs_get_user_vip ( index ) 
Type
Native 
Notes
index is a player index from 1 to 32.   

User Contributed Notes
Freeecode at hotmail dot com | Jun-24-04 20:40:42  
---|---  
Here is a small code that will show everyone who VIP is. `    
new players[32],inum;   
get_players(players,inum);   
for(new x=0; x <= inum; x++)   
{   
     if(cs_get_user_vip(players[x])   
     {   
          //This user is VIP   
     }   
}   
  `  
  

