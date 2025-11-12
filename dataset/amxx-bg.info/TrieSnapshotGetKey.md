# TrieSnapshotGetKey
#### Syntax
```
native TrieSnapshotGetKey(Snapshot:handle, index, buffer[], maxlength);
```

#### Usage
handle | ```Map snapshot handle```
---|---
index | ```Key index (starting from 0)```
buffer | ```String buffer```
maxlength | ```Maximum buffer length```
#### Description
```
Retrieves the key string of a given key in a map snapshot.
```

#### Return
```
Number of bytes written to the buffer
```

#### Error
```
If an invalid handle is provided an error will be
thrown. or index out of range
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

