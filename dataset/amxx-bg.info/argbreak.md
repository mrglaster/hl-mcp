# argbreak
#### Syntax
```
stock argbreak(const text[], left[], leftlen, right[], rightlen)
```

#### Usage
text | ```Source input string.```
---|---
left | ```Buffer to store string left part.```
leftlen | ```Maximum length of the string part buffer.```
right | ```Buffer to store string right part.```
rightlen | ```Maximum length of the string part buffer.```
#### Description
```
Emulates strbreak() using argparse().
```

#### Return
```
-1 if no match was found; otherwise, an index into source
marking the first index after the searched text.  The
index is always relative to the start of the input string.
```


This code is a part of string_stocks.inc. To use this code you should include string_stocks.inc as ```#include <string_stocks>```


  
  

