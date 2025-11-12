# contain
#### Syntax
```
native contain(const source[], const string[]);
```

#### Usage
source | ```String to search in.```
---|---
string | ```Substring to find inside the original string.```
#### Description
```
Tests whether a string is found inside another string.
```

#### Return
```
-1 on failure (no match found). Any other value
indicates a position in the string where the match starts.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

