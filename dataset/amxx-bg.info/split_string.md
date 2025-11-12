# split_string
#### Syntax
```
native split_string(const source[], const split[], part[], partLen);
```

#### Usage
source | ```Source input string.```
---|---
split | ```A string which specifies a search point to break at.```
part | ```Buffer to store string part.```
partLen | ```Maximum length of the string part buffer.```
#### Description
```
Returns text in a string up until a certain character sequence is reached.
```

#### Note
```
Only available in 1.8.3 and above.
```

#### Return
```
-1 if no match was found; otherwise, an index into source
marking the first index after the searched text.  The
index is always relative to the start of the input string.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

