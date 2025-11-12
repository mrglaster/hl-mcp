# get_gametime
#### Syntax
```
native Float:get_gametime();
```

#### Description
```
Returns the game time based on the game tick.
```

#### Note
```
This time is counted up from map start. If the engine is not processing
this function will return the same value between calls, which makes it
unusable for profiling purposes.
```

#### Return
```
Game time, in seconds
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

