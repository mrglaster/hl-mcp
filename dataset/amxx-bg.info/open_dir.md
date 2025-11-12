# open_dir
#### Syntax
```
native open_dir(dir[], firstfile[], length, &FileType:type = FileType_Unknown, bool:use_valve_fs = false, const valve_path_id[] = "GAME");
```

#### Usage
dir | ```Path to open.```
---|---
firstfile | ```String buffer to hold first file name```
length | ```Maximum size of the string buffer```
type | ```Optional variable to store the file type```
use_valve_fs | ```If true, the Valve file system will be used instead. This can be used to find files existing in any of the Valve search paths, rather than solely files existing directly in the gamedir.```
valve_path_id | ```If use_valve_fs, a search path from gameinfo or NULL_STRING for all search paths.```
#### Description
```
Opens a directory/folder for contents enumeration.
```

#### Note
```
Directories are closed with close_dir().
```

#### Return
```
Handle to the directory, 0 otherwise
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

