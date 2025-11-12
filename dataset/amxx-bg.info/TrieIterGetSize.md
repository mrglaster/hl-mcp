# TrieIterGetSize
#### Syntax
```
native TrieIterGetSize(TrieIter:handle);
```

#### Usage
handle | ```Iterator handle```
---|---
#### Description
```
Retrieves the number of elements in the underlying map.
```

#### Note
```
When used on a valid iterator this is exactly the same as calling TrieGetSize on the map directly.
```

#### Return
```
Number of elements in the map
```

#### Error
```
Invalid handle
Iterator has been closed (underlying map destroyed)
Iterator is outdated
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

