# TrieKeyExists
#### Syntax
```
native bool:TrieKeyExists(Trie:handle, const key[]);
```

#### Usage
handle | ```Map handle```
---|---
key | ```Key string```
#### Description
```
Checks a hash map for the existence of an entry.
```

#### Return
```
True if the key is set, false otherwise
```

#### Error
```
If an invalid handle is provided an error will be
thrown.
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

