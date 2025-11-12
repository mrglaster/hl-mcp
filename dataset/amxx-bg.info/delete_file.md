# delete_file
#### Syntax
```
native delete_file(const file[], bool:use_valve_fs = false, const valve_path_id[] = "GAMECONFIG");
```

#### Usage
file | ```Path of the file to delete```
---|---
use_valve_fs | ```If true, the Valve file system will be used instead. This can be used to delete files existing in the Valve search path, rather than solely files existing directly in the gamedir.```
valve_path_id | ```If use_valve_fs, a search path from gameinfo or NULL_STRING for all search paths.```
#### Description
```
Deletes a file.
```

#### Return
```
1 on success, 0 on failure or if file not immediately removed.
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

