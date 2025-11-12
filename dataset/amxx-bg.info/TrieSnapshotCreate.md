# TrieSnapshotCreate
#### Syntax
```
native Snapshot:TrieSnapshotCreate(Trie:handle);
```

#### Usage
handle | ```Map handle```
---|---
#### Description
```
Creates a snapshot of all keys in a hash map. If the map is changed
afterwards,  the changes are not reflected in the snapshot.
Keys are not sorted.
```

#### Return
```
New map snapshot handle, which must be freed via
TrieSnapshotDestroy()
```

#### Error
```
If an invalid handle is provided an error will be
thrown.
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

