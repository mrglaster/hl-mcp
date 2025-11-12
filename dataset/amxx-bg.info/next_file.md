# next_file
#### Syntax
```
native next_file(dirh, buffer[], length, &FileType:type = FileType_Unknown);
```

#### Usage
dirh | ```Handle to a directory```
---|---
buffer | ```String buffer to hold directory name```
length | ```Maximum size of string buffer```
type | ```Optional variable to store the file type. FileType_* constants```
#### Description
```
Reads the next directory entry as a local filename.
```

#### Note
```
Contents of buffers are undefined when returning false.
```

#### Note
```
Both the '.' and '..' automatic directory entries will be retrieved for Windows and Linux.
```

#### Return
```
1 on success, 0 if there are no more files to read.
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

