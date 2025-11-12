# TrieCreate
#### Syntax
```
native Trie:TrieCreate();
```

#### Description
```
Creates a hash map. A hash map is a container that maps strings (called keys)
to arbitrary values (cells, arrays or strings).
```

#### Note
```
Keys in a hash map are unique so there is no more than one entry in the
map for any given key.
```

#### Note
```
Insertion, deletion, and lookup in a hash map are all considered to be
fast operations, amortized to O(1), or constant time.
```

#### Return
```
New Map handle, which must be freed via TrieDestroy()
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

