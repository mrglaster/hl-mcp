# TrieIterGetArray
#### Syntax
```
native bool:TrieIterGetArray(TrieIter:handle, any:array[], outputsize, &size = 0);
```

#### Usage
handle | ```Iterator handle```
---|---
buffer | ```Buffer to store the array```
outputsize | ```Maximum size of buffer```
size | ```Optional parameter to store the number of bytes written to the buffer```
#### Description
```
Retrieves an array at the current position of the iterator.
```

#### Return
```
True on success, false if the iterator is empty or the current
value is not an array.
```

#### Error
```
Invalid handle
Invalid buffer size
Iterator has been closed (underlying map destroyed)
Iterator is outdated
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

