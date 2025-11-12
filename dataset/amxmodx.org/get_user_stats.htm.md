et_user_stats
[TSX](http://127.0.0.1:8000/content/index.htm) (tsstats.inc) 
Description
get_user_stats - Gets overall stats. 
Syntax
get_user_stats ( index, stats[8], bodyhits[8] ) 
Type
Native 
Notes
Gets overall stats which are stored in file on server and updated on every respawn or user disconnect. Function returns the position in stats by diff. kills to deaths.
