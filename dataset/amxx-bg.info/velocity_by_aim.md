# velocity_by_aim
#### Syntax
```
native velocity_by_aim(iIndex, iVelocity, Float:vRetValue[3]);
```

#### Usage
iIndex | ```Client index```
---|---
iVelocity | ```Multiply vRetValue length by this much```
vRetValue | ```Store the calculated velocity in this vector.```
#### Description
```
Calculates velocity in the direction player is looking.
```

#### Return
```
This function has no return value.
```

#### Error
```
If client is not connected or client index is not
within the range of 1 to MaxClients.
```


This code is a part of vector.inc. To use this code you should include vector.inc as ```#include <vector>```


  
  

