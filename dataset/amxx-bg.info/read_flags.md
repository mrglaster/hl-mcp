# read_flags
#### Syntax
```
native read_flags(const flags[]);
```

#### Usage
flags | ```Flag string to convert```
---|---
#### Description
```
Converts a flag string to a bitflag value.
```

#### Note
```
Example: The string "abcd" represents the sum of 1, 2, 4, and 8 - or
(1<<0)|(1<<1)|(1<<2)|(1<<3). The function will return 15.
```

#### Return
```
Bitflag value
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

