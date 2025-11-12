et_players
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_players - Returns a list of player indices. 
Syntax
get_players ( players[32], &num, const flags = ) 
Type
Native 
Notes
If specified, you can constrain which players are returned by flags:   
"a" - Don't return dead players   
"b" - Don't return alive players   
"c" - Skip bots   
"d" - Skip real players   
"e" - Match with passed team   
"f" - Match with part of name   
"g" - Ignore case sensitivity   
  
Example, Get dead players:`    
new Players[32]   
new playerCount, i, player   
get_players(Players, playerCount, "b")   
for (i=0; i<playerCount; i++)   
   player = Players[i]  `   
  
  
  

