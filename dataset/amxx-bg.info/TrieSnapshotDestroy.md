# TrieSnapshotDestroy
#### Syntax
```
native TrieSnapshotDestroy(&Snapshot:handle);
```

#### Usage
handle | ```Map snapshot handle```
---|---
#### Description
```
Destroys a map snapshot and frees its memory.
```

#### Note
```
The function automatically sets the variable passed to it to 0 to aid
in preventing accidental usage after destroy.
```

#### Return
```
1 on success, 0 if an invalid handle was passed in
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

