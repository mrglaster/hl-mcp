# TrieIterEnded
#### Syntax
```
native bool:TrieIterEnded(TrieIter:handle);
```

#### Usage
handle | ```Iterator handle```
---|---
#### Description
```
Returns if the iterator has reached its end and no more data can be read.
```

#### Return
```
True if iterator has reached the end, false otherwise
```

#### Error
```
Invalid Handle
Iterator has been closed (underlying map destroyed)
Iterator is outdated
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

