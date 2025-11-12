# get_usercmd
#### Syntax
```
native get_usercmd(type, any:...);
```

#### Usage
type | ```Entry to retrieve from```
---|---
... | ```Depending on the entry type a different number of additional parameters should be provided:    int      - Returns the entry integer value directly, no               additional parameters required    float    - Stores the entry float value into the               variable provided as the second parameter    vector   - Copies the entry vector to the Float:array[3]               provided in the second parameter```
#### Description
```
Retrieves a value from a usercmd struct.
```

#### Note
```
This native can only be used inside the client_cmdStart() forward. If
it is used outside this forward it will not retrieve any results and
always return 0.
```

#### Note
```
For a list of valid usercmd entries see the usercmd_* constants in
engine_const.inc
```

#### Return
```
Changes depending on the entry type:
   int      - Returns the entry integer value
   float    - Returns 1
   vector   - Returns 1
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

