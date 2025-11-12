# FileReadUint8
#### Syntax
```
native bool:FileReadUint8(file, &any:data);
```

#### Usage
file | ```Handle to the file```
---|---
data | ```Variable to store the data read```
#### Description
```
Reads a single uint8 (unsigned byte) from a file. The returned value is
zero-extended to an int32.
```

#### Return
```
True on success, false on failure
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

