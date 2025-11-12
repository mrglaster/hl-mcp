# fwrite_blocks
#### Syntax
```
native fwrite_blocks(file, const any:data[], blocks, mode);
```

#### Usage
file | ```Handle to the file```
---|---
data | ```Array of items to write```
blocks | ```Number of items in the array```
mode | ```Size of each item in the array in bytes Valid sizes are 1, 2, or 4. See BLOCK_* constants```
#### Description
```
Writes binary data to a file.
```

#### Return
```
Number of elements written
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

