# file_size
#### Syntax
```
native file_size(const file[], flag = FSOPT_BYTES_COUNT, bool:use_valve_fs = false, const valve_path_id[] = "GAME");
```

#### Usage
file | ```Path to the file```
---|---
flag | ```Flag options, see FSOPT_* constants```
use_valve_fs | ```If true, the Valve file system will be used instead. This can be used to find files existing in any of the Valve search paths, rather than solely files existing directly in the gamedir. If used, flag option is ignored.```
valve_path_id | ```If use_valve_fs, a search path from gameinfo or NULL_STRING for all search paths```
#### Description
```
Get the file size in bytes.
```

#### Return
```
If flag is FSOPT_BYTES_COUNT or use_valve_fs to true, the file size in bytes
If flag is FSOPT_LINES_COUNT, the number of lines in the file
If flag is FSOPT_END_WITH_LF, 1 is returned if file ends with line feed
If file doesn't exist, -1
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

