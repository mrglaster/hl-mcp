# fread_blocks
#### Syntax
```
native fread_blocks(file, any:data[], blocks, mode);
```

#### Usage
file | ```Handle to the file```
---|---
data | ```Array to store each item read```
blocks | ```Number of items to read into the array```
mode | ```Size of each element, in bytes, to be read Valid sizes are 1, 2, or 4. See BLOCK_* constants.```
#### Description
```
Reads binary data from a file.
```

#### Return
```
Number of elements read
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

