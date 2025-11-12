# fread_raw
#### Syntax
```
native fread_raw(file, any:stream[], blocksize, blocks);
```

#### Usage
file | ```Handle to the file```
---|---
stream | ```Array to store each item read```
blocksize | ```Number of items to read into the array```
blocks | ```Size of each element, in bytes. The data is read directly. That is, in 1 or 2-byte mode, the lower byte(s) in each cell are used directly, rather than performing any casts from a 4-byte number to a smaller number.```
#### Description
```
Reads raw binary data from a file.
```

#### Return
```
Number of elements read
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

