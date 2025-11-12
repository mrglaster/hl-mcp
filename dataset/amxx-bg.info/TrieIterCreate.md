# TrieIterCreate
#### Syntax
```
native TrieIter:TrieIterCreate(Trie:handle);
```

#### Description
```
Creates an iterator for a map. It provides iterative read-only access to the
maps contents.
```

#### Note
```
Removing or adding keys to the underlying map will invalidate all its
iterators. Updating values of existing keys is allowed and the changes
will be immediately reflected in the iterator.
```

#### Note
```
Iterators are designed to be short-lived and not stored, and creating
them is very cheap. Reading data from an iterator is just as fast as
reading directly from the map.
```

#### Note
```
Just like in snapshots the keys are not sorted.
```

#### Return
```
New iterator handle, which must be freed via TrieIterDestroy().
```

#### Error
```
Invalid Handle
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

