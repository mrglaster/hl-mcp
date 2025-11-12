# fwrite
#### Syntax
```
native fwrite(file, any:data, mode);
```

#### Usage
file | ```Handle to the file```
---|---
data | ```Item to write```
mode | ```Size of each item in the array in bytes Valid sizes are 1, 2, or 4. See BLOCK_* constants```
#### Description
```
Writes a single binary data to a file.
```

#### Return
```
Number of elements written
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

