# read_argv
#### Syntax
```
native read_argv(id, output[], len);
```

#### Usage
id | ```Argument index starting from 1, 0 returns the command itself```
---|---
output | ```Buffer to copy command argument to```
len | ```Maximum buffer size```
#### Description
```
Retrieves argument of client command as string.
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


  
  

