# hash_string
#### Syntax
```
native hash_string(const string[], const HashType:type, output[], const outputSize);
```

#### Usage
string | ```String to be hashed.```
---|---
type | ```Type of selected hashing algorithm. See Hash_* constants in amxconst.inc file.```
output | ```Output string to store hash in.```
outputSize | ```The maximum size of the output string to store hash in.```
#### Description
```
Generate a hash value (message digest)
```

#### Return
```
Number of written bytes.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

