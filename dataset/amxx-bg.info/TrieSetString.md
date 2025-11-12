# TrieSetString
#### Syntax
```
native TrieSetString(Trie:handle, const key[], const value[], bool:replace = true);
```

#### Usage
handle | ```Map handle```
---|---
key | ```Key string```
value | ```String to store```
replace | ```If false the operation will fail if the key is already set```
#### Description
```
Sets a string value in a hash map, either inserting a new entry or replacing
an old one.
```

#### Return
```
1 on success, 0 otherwise
```

#### Error
```
If an invalid handle is provided an error will be
thrown.
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

