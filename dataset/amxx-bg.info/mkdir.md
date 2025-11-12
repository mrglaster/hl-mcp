# mkdir
#### Syntax
```
native mkdir(const dirname[], mode = FPERM_DIR_DEFAULT, bool:use_valve_fs = false, const valve_path_id[] = "GAMECONFIG");
```

#### Usage
path | ```Path to create```
---|---
mode | ```Permissions (default is o=rx,g=rx,u=rwx).  Note that folders must have the execute bit set on Linux.  On Windows, the mode is ignored.```
use_valve_fs | ```If true, the Valve file system will be used instead This can be used to create folders in the game's Valve search paths, rather than directly in the gamedir.```
valve_path_id | ```If use_valve_fs, a search path from gameinfo or NULL_STRING for default In this case, mode is ignored```
#### Description
```
Creates a directory.
```

#### Return
```
0 on success, -1 otherwise
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

