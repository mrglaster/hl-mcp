et_user_vstats
[TSX](http://127.0.0.1:8000/content/index.htm) (tsstats.inc) 
Description
get_user_vstats - Gets stats with which user have killed/hurt his victim. 
Syntax
get_user_vstats ( index, victim, stats[8], bodyhits[8], [ wpnname[] = "", len = 0 ] ) 
Type
Native 
Notes
Gets stats with which user have killed/hurt his victim. If victim is 0 then stats are from all victims. If victim has not been hurt, function returns 0 in other case 1. User stats are reset on his respawn.
