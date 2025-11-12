et_stats
[TSX](http://127.0.0.1:8000/content/index.htm) (tsstats.inc) 
Description
get_stats - Gets overall stats. 
Syntax
get_stats ( index, stats[8], bodyhits[8], name[], len ) 
Type
Native 
Notes
Gets overall stats which stored in stats.dat file in amx folder and updated on every mapchange or user disconnect. Function returns next index of stats entry or 0 if no more exists.
