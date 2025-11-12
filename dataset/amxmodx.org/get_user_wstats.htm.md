et_user_wstats
[TSX](http://127.0.0.1:8000/content/index.htm) (tsstats.inc) 
Description
get_user_wstats - Gets stats from given weapon index. 
Syntax
get_user_wstats ( index, wpnindex, stats[8], bodyhits[8] ) 
Type
Native 
Notes
Gets stats from given weapon index. If wpnindex is 0 then the stats are from all weapons. If weapon has not been used function returns 0 in other case 1. Fields in stats are:   
0 - kills   
1 - deaths   
2 - headshots   
3 - teamkilling   
4 - shots   
5 - hits   
6 - damage   
For body hits fields see amxconst.inc.
