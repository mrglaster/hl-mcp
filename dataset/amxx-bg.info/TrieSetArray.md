# TrieSetArray
#### Syntax
```
native TrieSetArray(Trie:handle, const key[], const any:buffer[], size, bool:replace = true);
```

#### Usage
handle | ```Map handle```
---|---
key | ```Key string```
buffer | ```Array to store```
size | ```Array size```
replace | ```If false the operation will fail if the key is already set```
#### Description
```
Sets an array value in a hash map, either inserting a new entry or replacing
an old one.
```

#### Return
```
1 on success, 0 otherwise
```

#### Error
```
If an invalid handle is provided an error will be
thrown. or invalid array size
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

