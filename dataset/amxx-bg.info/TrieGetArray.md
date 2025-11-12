# TrieGetArray
#### Syntax
```
native bool:TrieGetArray(Trie:handle, const key[], any:output[], outputsize, &size = 0);
```

#### Usage
handle | ```Map handle```
---|---
key | ```Key string```
output | ```Array to copy the value to```
outputsize | ```Maximum size of array```
size | ```Optional variable to store the number of cells written to the array in```
#### Description
```
Retrieves a string from a hash map.
```

#### Return
```
True on success, false if either the key is not set or
the value type does not match (value is cell or string)
```

#### Error
```
If an invalid handle or array size is provided an error
will be thrown.
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

