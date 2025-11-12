# fputs
#### Syntax
```
native fputs(file, const text[], bool:null_term = false);
```

#### Usage
file | ```Handle to the file```
---|---
text | ```String to write```
null_term | ```True to append NULL terminator, false otherwise```
#### Description
```
Writes a line of text to a text file.
```

#### Return
```
0 on success, -1 otherwise
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

