# hash_file
#### Syntax
```
native hash_file(const fileName[], const HashType:type, output[], const outputSize);
```

#### Usage
fileName | ```Path of file to be hashed.```
---|---
type | ```Type of selected hashing algorithm. See Hash_* constants in amxconst.inc file.```
output | ```Output string to store hash in.```
outputSize | ```The maximum size of the output string to store hash in.```
#### Description
```
Generate a hash value using the contents of a given file
```

#### Return
```
Number of written bytes.
```

#### Error
```
If the file couldn't be opened, an error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

