# TrieGetString
#### Syntax
```
native bool:TrieGetString(Trie:handle, const key[], output[], outputsize, &size = 0);
```

#### Usage
handle | ```Map handle```
---|---
key | ```Key string```
output | ```Buffer to copy the value to```
outputsize | ```Maximum size of buffer```
size | ```Optional variable to store the number of cells written to the buffer in```
#### Description
```
Retrieves a string from a hash map.
```

#### Return
```
True on success, false if either the key is not set or
the value type does not match (value is cell or array)
```

#### Error
```
If an invalid handle is provided an error will be
thrown.
```


This code is a part of celltrie.inc. To use this code you should include celltrie.inc as ```#include <celltrie>```


  
  

