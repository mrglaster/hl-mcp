# find_player
#### Syntax
```
native find_player(const flags[], ...);
```

#### Usage
flags | ```List of filtering flags:   "a" - match with name   "b" - match with name substring   "c" - match with authid   "d" - match with ip   "e" - match with team name   "f" - do not include dead clients   "g" - do not include alive clients   "h" - do not include bots   "i" - do not include human clients   "j" - return last matched client instead of the first   "k" - match with userid   "l" - match case insensitively   "m" - include connecting clients```
---|---
... | ```String to match against (integer if "k" flag is specified)```
#### Description
```
Find a player given a filter.
```

#### Note
```
Please consider using find_player_ex() instead which allows you to
use named constants for flags instead of letters.
```

#### Note
```
If matching by userid, do not also specify the "a", "b" or "c" flags,
or the function may not return a correct result.
```

#### Return
```
Client index, or 0 if no client was found
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

