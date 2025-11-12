# LoadFileForMe
#### Syntax
```
native LoadFileForMe(const file[], buffer[], maxlength, &length = 0);
```

#### Usage
file | ```File to load (may be a file from the GCF)```
---|---
buffer | ```Buffer to store file contents```
maxlength | ```Maximum size of the file buffer```
length | ```Variable to store the file length.  This may return a number larger than the buffer size```
#### Description
```
Loads a file using the LoadFileForMe engine function.

The data is truncated if there is not enough space.  No null-terminator
is applied; the data is the raw contents of the file.
```

#### Return
```
-1 if the file could not be loaded.  Otherwise,
the number of cells actually written to the buffer
are returned.
```


This code is a part of file.inc. To use this code you should include file.inc as ```#include <file>```


  
  

