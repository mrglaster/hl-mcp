# fwrite_raw
#### Syntax
```
native fwrite_raw(file, const any:stream[], blocks, mode);
```

#### Usage
file | ```Handle to the file.```
---|---
stream | ```Array of items to write.  The data is written directly. That is, in 1 or 2-byte mode, the lower byte(s) in each cell are used directly, rather than performing any casts from a 4-byte number to a smaller number.```
blocks | ```Size of each item in the array in bytes.```
mode | ```Number of items in the array.```
#### Description
```
Writes raw binary data to a file.
```

#### Return
```
Number of elements written
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

