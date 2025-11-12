# lookup_sequence
#### Syntax
```
native lookup_sequence(entity, const name[], &Float:framerate = 0.0, &bool:loops = false, &Float:groundspeed = 0.0);
```

#### Usage
entity | ```The entity id to lookup.```
---|---
name | ```The sequence name to lookup, case insensitive. ("JUMP" would match "jump")```
framerate | ```The framerate of the sequence, if found.```
loops | ```Whether or not the sequence loops.```
groundspeed | ```The groundspeed setting of the sequence.```
#### Description
```
Looks up the sequence for the entity.
```

#### Return
```
-1 on failed lookup, the sequence number on successful lookup.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

