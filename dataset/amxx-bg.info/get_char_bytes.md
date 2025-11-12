# get_char_bytes
#### Syntax
```
native get_char_bytes(const source[]);
```

#### Usage
source | ```Source input string.```
---|---
#### Description
```
Returns the number of bytes a character is using.  This is
for multi-byte characters (UTF-8).  For normal ASCII characters,
this will return 1.
```

#### Note
```
Only available in 1.8.3 and above.
```

#### Return
```
Number of bytes the current character uses.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

