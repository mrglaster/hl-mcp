# get_players_ex
#### Syntax
```
stock get_players_ex(players[MAX_PLAYERS] = {}, &num, GetPlayersFlags:flags = GetPlayers_None, const team[] = "")
```

#### Usage
players | ```Array to store indexes to```
---|---
num | ```Variable to store number of indexes to```
flags | ```Optional filtering flags (enum GetPlayersFlags); valid flags are:   GetPlayers_None - No filter (Default)   GetPlayers_ExcludeDead - do not include dead clients   GetPlayers_ExcludeAlive - do not include alive clients   GetPlayers_ExcludeBots - do not include bots   GetPlayers_ExcludeHuman - do not include human clients   GetPlayers_MatchTeam - match with team   GetPlayers_MatchNameSubstring - match with part of name   GetPlayers_CaseInsensitive - match case insensitive   GetPlayers_ExcludeHLTV - do not include HLTV proxies   GetPlayers_IncludeConnecting - include connecting clients```
team | ```String to match against if the "e" or "f" flag is specified```
#### Description
```
Stores a filtered list of client indexes to an array.
```

#### Note
```
Example retrieving all alive CTs:
get_players_ex(players, num, GetPlayers_ExcludeDead | GetPlayers_MatchTeam, "CT")
```

#### Return
```
This function has no return value.
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

