# strncmp
#### Syntax
```
native strncmp(const string1[], const string2[], num, bool:ignorecase = false);
```

#### Usage
string1 | ```First string (left).```
---|---
string2 | ```Second string (right).```
num | ```Number of characters to compare.```
ignorecase | ```If true, comparison is case insensitive. If false (default), comparison is case sensitive.```
#### Description
```
Compares two strings parts lexographically.
```

#### Note
```
Only available in 1.8.3 and above.
```

#### Note
```
This supports multi-byte characters (UTF-8) on case insensitive comparison.
```

#### Return
```
-1 if string1 < string2
0 if string1 == string2
1 if string1 > string2
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

