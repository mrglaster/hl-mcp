# playback_event
#### Syntax
```
native playback_event(flags, invoker, eventindex, Float:delay, const Float:origin[3], const Float:angles[3], Float:fparam1, Float:fparam2, iparam1, iparam2, bparam1, bparam2);
```

#### Usage
flags | ```Event flags```
---|---
invoker | ```Index of entity to invoke event on```
eventindex | ```Index of event in the precache table```
delay | ```Time until the event is played```
origin | ```Origin to play event from```
angles | ```Angles to play event with```
fparam1 | ```Float parameter 1 to pass along into/with the event```
fparam2 | ```Float parameter 2 to pass along into/with the event```
iparam1 | ```Integer parameter 1 to pass along into/with the event```
iparam2 | ```Integer parameter 2 to pass along into/with the event```
bparam1 | ```Boolean parameter 1 to pass along into/with the event```
bparam2 | ```Boolean parameter 2 to pass along into/with the event```
#### Description
```
Plays back an event on the client. Most prominently used for gun firing
animations.
```

#### Note
```
Event indexes can be acquired using precache_event() with the sc dummy
files in the events folder.
```

#### Return
```
This function has no return value.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

