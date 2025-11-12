et_user_astats
[TSX](http://127.0.0.1:8000/content/index.htm) (tsstats.inc) 
Description
get_user_astats - Gets stats with which user have been killed/hurt. 
Syntax
get_user_astats ( index, wpnindex, stats[8], bodyhits[8], [ wpnname[] = "", len = 0 ] ) 
Type
Native 
Notes
Gets stats with which user have been killed/hurt. If killer is 0 then stats are from all attacks. If killer has not hurt user, function returns 0 in other case 1. User stats are reset on his respawn.
