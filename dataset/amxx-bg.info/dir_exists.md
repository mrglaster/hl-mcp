# dir_exists
#### Syntax
```
native dir_exists(const dir[], bool:use_valve_fs = false);
```

#### Usage
dir | ```Path to the directory```
---|---
use_valve_fs | ```If true, the Valve file system will be used instead. This can be used to find files existing in any of the Valve search paths, rather than solely files existing directly in the gamedir.```
#### Description
```
Checks if a directory exists.
```

#### Return
```
1 if the directory exists, 0 otherwise
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

