# get_playersnum_ex
#### Syntax
```
stock get_playersnum_ex(GetPlayersFlags:flags = GetPlayers_None, const team[] = "")
```

#### Usage
flags | ```Optional filtering flags (enum GetPlayersFlags); valid flags are:   GetPlayers_None - No filter (Default)   GetPlayers_ExcludeDead - do not include dead clients   GetPlayers_ExcludeAlive - do not include alive clients   GetPlayers_ExcludeBots - do not include bots   GetPlayers_ExcludeHuman - do not include human clients   GetPlayers_MatchTeam - match with team   GetPlayers_MatchNameSubstring - match with part of name   GetPlayers_CaseInsensitive - match case insensitive   GetPlayers_ExcludeHLTV - do not include HLTV proxies   GetPlayers_IncludeConnecting - include connecting clients```
---|---
team | ```String to match against if the GetPlayers_MatchTeam or GetPlayers_MatchNameSubstring flag is specified```
#### Description
```
Returns the number of clients on the server that match the specified flags.
```

#### Note
```
Example retrieving all alive CTs:
new AliveCt = get_playersnum_ex(GetPlayers_ExcludeDead | GetPlayers_MatchTeam, "CT")
```

#### Return
```
Number of clients on the server that match the specified flags
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

