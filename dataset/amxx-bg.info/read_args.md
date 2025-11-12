# read_args
#### Syntax
```
native read_args(output[], len);
```

#### Usage
output | ```Buffer to copy command line to```
---|---
len | ```Maximum buffer size```
#### Description
```
Retrieves full client command string.
```

#### Note
```
Should only be used inside of the client_command() forward.
```

#### Return
```
Number of cells written to buffer
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

