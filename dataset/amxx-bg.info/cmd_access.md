# cmd_access
#### Syntax
```
stock cmd_access(id, level, cid, num, bool:accesssilent = false)
```

#### Usage
id | ```Client index```
---|---
level | ```Required admin flags```
cid | ```Command id```
num | ```Required number of parameters```
acesssilent | ```If true no denied access message will be printed```
#### Description
```
Returns if the user can execute the current command by checking the necessary
admin flags and parameter count. Displays a denied access message to the user
if missing privileges or a usage example if too few parameters are provided.
```

#### Note
```
This should be used inside of a command forward as it uses read_argc()
to check the parameter count.
```

#### Return
```
1 if access granted and parameters provided, 0 otherwise
```


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

