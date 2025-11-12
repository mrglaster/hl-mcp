# read_file
#### Syntax
```
native read_file(const file[], line, text[], len, &txtlen = 0);
```

#### Usage
file | ```Path to open```
---|---
line | ```Index of the line, starting to 0```
text | ```String buffer to hold line read```
len | ```Maximum size of string buffer```
txtlen | ```Number of characters written to the buffer```
#### Description
```
Reads line from file.
```

#### Note
```
This native is expensive. Consider the use of new file natives (fopen(), fgets(), etc.)
if purpose is to read several lines of a file.
```

#### Return
```
Returns index of next line, otherwise 0 when end of file is reached
```

#### Error
```
Unable to read the file
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

