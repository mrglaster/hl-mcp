# strcmp
#### Syntax
```
native strcmp(const string1[], const string2[], bool:ignorecase = false);
```

#### Usage
string1 | ```First string (left).```
---|---
string2 | ```Second string (right).```
ignorecase | ```If true, comparison is case insensitive. If false (default), comparison is case sensitive.```
#### Description
```
Compares two strings lexographically.
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


  
  

