# strtok2
#### Syntax
```
native strtok2(const text[], left[], const llen, right[], const rlen, const token = ' ', const trim = 0);
```

#### Usage
text | ```String to tokenize```
---|---
left | ```Buffer to store left half```
llen | ```Size of left buffer```
right | ```Buffer to store right half```
rlen | ```Size of right buffer```
token | ```Token to split by```
trim | ```Flags for trimming behavior, see above```
#### Description
```
Breaks a string in two by token.
```

#### Note
```
Only available in 1.8.3 and above.
```

#### Return
```
Returns position of token in string if found,
-1 if token was not found
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

