# TrieDeleteKey
#### Syntax
```
native bool:TrieDeleteKey(Trie:handle, const key[]);
```

#### Usage
handle | ```Map handle```
---|---
key | ```Key string```
#### Description
```
Removes an entry from a hash map.
```

#### Return
```
True on success, false if the key was never set
```

#### Error
```
If an invalid handle is provided an error will be
thrown.
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

