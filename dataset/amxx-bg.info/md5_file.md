# md5_file
#### Syntax
```
#pragma deprecated Use hash_file() function. Also, see Hash_* constants.
native md5_file(const file[], md5buffer[34]);
```

#### Usage
file | ```Path to file to calculate keysum of```
---|---
md5buffer | ```Buffer to copy the MD5 hash to```
#### Description
```
Calculates the MD5 keysum of a file.
```

#### Return
```
Number of cells written to the buffer (always 32)
```

#### Error
```
If the file can not be opened, and error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

