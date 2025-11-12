# get_players
#### Syntax
```
native get_players(players[MAX_PLAYERS], &num, const flags[] = "", const team[] = "");
```

#### Usage
players | ```Array to store indexes to```
---|---
num | ```Variable to store number of indexes to```
flags | ```Optional list of filtering flags:   "a" - do not include dead clients   "b" - do not include alive clients   "c" - do not include bots   "d" - do not include human clients   "e" - match with team   "f" - match with part of name   "g" - match case insensitive   "h" - do not include HLTV proxies   "i" - include connecting clients```
team | ```String to match against if the "e" or "f" flag is specified```
#### Description
```
Stores a filtered list of client indexes to an array.
```

#### Note
```
Please consider using get_players_ex() instead which allows you to
use named constants for flags instead of letters.
```

#### Note
```
Example retrieving all alive CTs: get_players(players, num "ae", "CT")
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

