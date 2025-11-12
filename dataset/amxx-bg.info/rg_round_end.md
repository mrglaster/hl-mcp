# rg_round_end
#### Syntax
```
native rg_round_end(const Float:tmDelay, const WinStatus:st, const ScenarioEventEndRound:event = ROUND_NONE, const message[] = "default", const sentence[] = "default", const bool:trigger = false);
```

#### Usage
tmDelay | ```Delay before the onset of a new round```
---|---
st | ```Which team won```
event | ```The event is the end of the round```
message | ```The message on round end```
sentence | ```The sound at the end of the round```
trigger | ```This will trigger to all hooks on that function Be very careful about recursion!```
#### Description
```
Forces the round to end.
```

#### Return
```
1 on success, 0 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.