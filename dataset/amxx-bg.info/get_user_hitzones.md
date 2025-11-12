# get_user_hitzones
#### Syntax
```
native get_user_hitzones(index, target);
```

#### Usage
index | ```Client index```
---|---
target | ```The target player```
#### Description
```
Gets the set of hit zone "rules" between @index and @target players.
```

#### Note
```
For the body part bitsum, see HITZONE* constants.
```

#### Return
```
The bitsum of @target's body parts @index is able to hit
```

#### Error
```
If player is not connected or not within the range
of 1 to MaxClients.
```


This code is a part of fun.inc. To use this code you should include fun.inc as ```#include <fun>```


  
  

