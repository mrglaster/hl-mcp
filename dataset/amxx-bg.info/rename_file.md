# rename_file
#### Syntax
```
native rename_file(const oldname[], const newname[], relative = 0);
```

#### Usage
oldname | ```New path to the file```
---|---
newname | ```Path to the existing file```
relative | ```If true, native  will act like other natives which use the moddir as a base directory. Otherwise, the current directory is undefined (but assumed to be hlds).```
#### Description
```
Renames a file.
```

#### Return
```
1 on success, 0 otherwise
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

