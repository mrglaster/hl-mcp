# TerminateRound
#### Syntax
```
native TerminateRound( const roundEndType, const teamWinning = TeamWinning_None, const mapType = MapType_AutoDetect );
```

#### Usage
roundEndType | ```The round end type you want to force.  @param teamWinning      The team winning if the round type end is either team extermination or objective.  @param mapType          The map type if there are severals objectives on the map.```
---|---
#### Description
```
Force a round to end whatever the conditions.

 Here all the possibilities of this native,
 to avoid further questions :

     // Time is up / round draw.

     TerminateRound( RoundEndType_Timer );
     TerminateRound( RoundEndType_Draw );

     // One of the team has been exterminated.

     TerminateRound( RoundEndType_TeamExtermination, TeamWinning_Terrorist );
     TerminateRound( RoundEndType_TeamExtermination, TeamWinning_Ct );

     // The current map objective of the team has been completed.

     TerminateRound( RoundEndType_Objective, TeamWinning_Terrorist );
     TerminateRound( RoundEndType_Objective, TeamWinning_Ct );

     // The provided map objective of the team has been completed. (will work only if the related entity is present)

     TerminateRound( RoundEndType_Objective, TeamWinning_Terrorist, MapType_VipAssasination );
     TerminateRound( RoundEndType_Objective, TeamWinning_Terrorist, MapType_Bomb );
     TerminateRound( RoundEndType_Objective, TeamWinning_Terrorist, MapType_PrisonEscape );
     TerminateRound( RoundEndType_Objective, TeamWinning_Ct, MapType_VipAssasination );
     TerminateRound( RoundEndType_Objective, TeamWinning_Ct, MapType_Bomb );
     TerminateRound( RoundEndType_Objective, TeamWinning_Ct, MapType_Hostage );
     TerminateRound( RoundEndType_Objective, TeamWinning_Ct, MapType_PrisonEscape );
```


This code is a part of round_terminator.inc. To use this code you should include round_terminator.inc as ```#include <round_terminator>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.