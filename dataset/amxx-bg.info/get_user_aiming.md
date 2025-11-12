# get_user_aiming
#### Syntax
```
native Float:get_user_aiming(index, &id, &body = HIT_GENERIC, dist = 9999);
```

#### Usage
index | ```Client index to trace aim from```
---|---
id | ```Variable to store hit client index (if applicable)```
body | ```Variable to store hit client body part (if applicable)```
dist | ```Maximum distance of the trace```
#### Description
```
Traces the client's current aim vector to see if it hits something.
```

#### Note
```
If the trace does not hit a client, id and body will be set to 0.
```

#### Note
```
If the trace hits nothing within the specified distance, 0 is returned.
```

#### Note
```
For a list of possible body hitplaces see the HIT_* constants in amxconst.inc.
```

#### Return
```
Distance between the trace start and end point
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

