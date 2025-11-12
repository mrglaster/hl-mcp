# pfn_playbackevent
#### Syntax
```
forward pfn_playbackevent(flags, entid, eventid, Float:delay, Float:Origin[3], Float:Angles[3], Float:fparam1, Float:fparam2, iparam1, iparam2, bparam1, bparam2);
```

#### Usage
flags | ```Event flags```
---|---
entid | ```Index of entity to invoke event on```
eventid | ```Index of event in the precache table```
delay | ```Time until the event is played```
Origin | ```Origin to play event from```
Angles | ```Angles to play event with```
fparam1 | ```Float parameter 1 to pass along into/with the event```
fparam2 | ```Float parameter 2 to pass along into/with the event```
iparam1 | ```Integer parameter 1 to pass along into/with the event```
iparam2 | ```Integer parameter 2 to pass along into/with the event```
bparam1 | ```Boolean parameter 1 to pass along into/with the event```
bparam2 | ```Boolean parameter 2 to pass along into/with the event```
#### Description
```
Called when an event is played.
```

#### Return
```
PLUGIN_CONTINUE to ignore, PLUGIN_HANDLED or higher to block
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

