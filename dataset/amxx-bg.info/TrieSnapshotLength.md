# TrieSnapshotLength
#### Syntax
```
native TrieSnapshotLength(Snapshot:handle);
```

#### Usage
handle | ```Map snapshot handle```
---|---
#### Description
```
Returns the number of keys in a map snapshot. Note that this may be
different from the size of the map, since the map can change after the
snapshot of its keys was taken.
```

#### Return
```
Number of keys
```

#### Error
```
If an invalid handle is provided an error will be
thrown.
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

