# TrieSnapshotKeyBufferSize
#### Syntax
```
native TrieSnapshotKeyBufferSize(Snapshot:handle, index);
```

#### Usage
handle | ```Map snapshot handle```
---|---
index | ```Key index (starting from 0)```
#### Description
```
Returns the buffer size required to store a given key. That is, it returns
the length of the key plus one.
```

#### Return
```
Buffer size required to store the key string
```

#### Error
```
If an invalid handle is provided an error will be
thrown. or index out of range
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

