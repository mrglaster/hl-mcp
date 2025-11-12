# read_dir
#### Syntax
```
native read_dir(const dirname[], pos, output[], len, &outlen = 0);
```

#### Usage
dirname | ```Path to open```
---|---
pos | ```Index the element```
output | ```String buffer to hold content```
len | ```Maximum size of string buffer```
outlen | ```Number of characters written to the buffer```
#### Description
```
Reads content from directory
```

#### Note
```
This native is expensive. Consider the use of open_dir(), next_file() and close_dir() instead.
```

#### Note
```
Both the '.' and '..' automatic directory entries will be retrieved for Windows and Linux.
```

#### Return
```
Returns index of next element, otherwiwe 0 when end of dir is reached
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

