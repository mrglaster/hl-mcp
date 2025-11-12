# strtok
#### Syntax
```
native strtok(const text[], Left[], leftLen, Right[], rightLen, token=' ', trimSpaces=0);
```

#### Usage
text | ```String to tokenize```
---|---
Left | ```Buffer to store left half```
leftLen | ```Size of left buffer```
Right | ```Buffer to store right half```
rightLen | ```Size of right buffer```
token | ```Token to split by```
trimSpaces | ```Whether spaces are trimmed.```
#### Description
```
Breaks a string in two by token.
```

#### Note
```
Trimming spaces is buggy. Consider strtok2 instead.
```

#### Note
```
See argbreak() for doing this with parameters.
Example:
 str1[] = This *is*some text
 strtok(str1, left, 24, right, 24, '*')
 left will be "This "
 Right will be "is*some text"
 If you use trimSpaces, all spaces are trimmed from Left.
```

#### Return
```
This function has no return value.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

