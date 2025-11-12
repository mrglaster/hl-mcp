# TrieIterGetString
#### Syntax
```
native bool:TrieIterGetString(TrieIter:handle, buffer[], outputsize, &size = 0);
```

#### Usage
handle | ```Iterator handle```
---|---
buffer | ```Buffer to store the string in```
outputsize | ```Maximum size of string buffer```
size | ```Optional parameter to store the number of bytes written to the buffer.```
#### Description
```
Retrieves a string at the current position of the iterator.
```

#### Return
```
True on success, false if the iterator is empty or the current value
is not a string.
```

#### Error
```
Invalid handle
Invalid buffer size
Iterator has been closed (underlying map destroyed)
Iterator is outdated
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

