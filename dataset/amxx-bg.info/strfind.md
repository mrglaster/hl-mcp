# strfind
#### Syntax
```
native strfind(const string[], const sub[], bool:ignorecase = false, pos = 0);
```

#### Usage
string | ```String to search in.```
---|---
sub | ```Substring to find inside the original string.```
ignorecase | ```If true, search is case insensitive. If false (default), search is case sensitive.```
pos | ```Start position to search from.```
#### Description
```
Tests whether a string is found inside another string.
```

#### Note
```
This supports multi-byte characters (UTF-8) on case insensitive comparison.
```

#### Return
```
-1 on failure (no match found). Any other value
indicates a position in the string where the match starts.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

