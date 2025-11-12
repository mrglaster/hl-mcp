# TrieIterGetKey
#### Syntax
```
native TrieIterGetKey(TrieIter:handle, key[], outputsize);
```

#### Usage
handle | ```Iterator handle.```
---|---
key | ```Buffer to store the current key in.```
outputsize | ```Maximum size of string buffer.```
#### Description
```
Retrieves the key the iterator currently points to.
```

#### Return
```
Nnumber of bytes written to the buffer
```

#### Error
```
Invalid handle
Iterator has been closed (underlying map destroyed)
Iterator is outdated
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

