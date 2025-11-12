# TrieGetCell
#### Syntax
```
native bool:TrieGetCell(Trie:handle, const key[], &any:value);
```

#### Usage
handle | ```Map handle```
---|---
key | ```Key string```
value | ```Variable to store value to```
#### Description
```
Retrieves a cell value from a hash map.
```

#### Return
```
True on success, false if either the key is not set or the
value type does not match (value is string or array)
```

#### Error
```
If an invalid handle is provided an error will be
thrown.
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

