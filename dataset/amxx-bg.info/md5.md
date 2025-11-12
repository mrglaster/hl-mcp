# md5
#### Syntax
```
#pragma deprecated Use hash_string() function. Also, see Hash_* constants.
native md5(const szString[], md5buffer[34]);
```

#### Usage
szString | ```String to calculate keysum of```
---|---
md5buffer | ```Buffer to copy the MD5 hash to```
#### Description
```
Calculates the MD5 keysum of a string.
```

#### Return
```
Number of cells written to the buffer (always 32)
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

