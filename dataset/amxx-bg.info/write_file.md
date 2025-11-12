# write_file
#### Syntax
```
native write_file(const file[], const text[], line = -1);
```

#### Usage
file | ```Path to open```
---|---
text | ```String to write to```
line | ```Index of the line, starting to 0 If < 0, content will be appended```
#### Description
```
Writes text to file.
```

#### Note
```
This native is expensive. Consider the use of new file natives (fopen(), fputs(), etc.)
if purpose is to write several lines of a file.
```

#### Return
```
This function has no return value.
```

#### Error
```
Unable to write [temporary] file
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

