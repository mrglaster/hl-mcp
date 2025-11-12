# FileReadInt8
#### Syntax
```
native bool:FileReadInt8(file, &any:data);
```

#### Usage
file | ```Handle to the file```
---|---
data | ```Variable to store the data read```
#### Description
```
Reads a single int8 (byte) from a file. The returned value is sign-
extended to an int32.
```

#### Return
```
True on success, false on failure
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

