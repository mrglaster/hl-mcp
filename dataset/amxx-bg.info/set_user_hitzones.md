# set_user_hitzones
#### Syntax
```
native set_user_hitzones(index = 0, target = 0, body = HITZONES_DEFAULT);
```

#### Usage
index | ```Client index```
---|---
target | ```The target player```
body | ```A bitsum of the body parts that can/can't be shot. See HITZONE* constants.```
#### Description
```
Sets (adds, removes) hit zones for a player.
```

#### Note
```
This actually sets rules of how any player can hit any other.
Example: set_user_hitzones(id, target, 2) - makes @id able to
hit @target only in the head.
```

#### Return
```
This function has no return value.
```

#### Error
```
If player is not connected or not within the range
of 1 to MaxClients.
```


This code is a part of fun.inc. To use this code you should include fun.inc as ```#include <fun>```


  
  

