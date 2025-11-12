# find_player_ex
#### Syntax
```
native find_player_ex(FindPlayerFlags:flags, ...);
```

#### Usage
flags | ```Filtering flags (enum FindPlayerFlags); valid flags are:   FindPlayer_MatchName - match with name   FindPlayer_MatchNameSubstring - match with name substring   FindPlayer_MatchAuthId - match with authid   FindPlayer_MatchIP - match with ip   FindPlayer_MatchTeam - match with team name   FindPlayer_ExcludeDead - do not include dead clients   FindPlayer_ExcludeAlive - do not include alive clients   FindPlayer_ExcludeBots - do not include bots   FindPlayer_ExcludeHuman - do not include human clients   FindPlayer_LastMatched - return last matched client instead of the first   FindPlayer_MatchUserId - match with userid   FindPlayer_CaseInsensitive - match case insensitively   FindPlayer_IncludeConnecting - include connecting clients```
---|---
... | ```String to match against (integer if FindPlayer_MatchUserId is specified)```
#### Description
```
Find a player given a filter.
```

#### Note
```
If matching by userid, do not also specify FindPlayer_MatchName, FindPlayer_MatchNameSubstring
or FindPlayer_MatchAuthId, or the function may not return a correct result.
```

#### Return
```
Client index, or 0 if no client was found
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

