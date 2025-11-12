# TrieIterGetCell
#### Syntax
```
native bool:TrieIterGetCell(TrieIter:handle, &any:value);
```

#### Usage
handle | ```Iterator handle```
---|---
value | ```Variable to store value in```
#### Description
```
Retrieves a value at the current position of the iterator.
```

#### Return
```
True on success, false if the iterator is empty or the current
value is an array or a string.
```

#### Error
```
Invalid handle
Iterator has been closed (underlying map destroyed)
Iterator is outdated
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

