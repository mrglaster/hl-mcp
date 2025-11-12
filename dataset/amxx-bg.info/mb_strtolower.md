# mb_strtolower
#### Syntax
```
native mb_strtolower(string[], maxlength = 0);
```

#### Usage
string | ```The string to convert.```
---|---
maxlength | ```Optional size of the buffer. If 0, the length of the original string will be used instead.```
#### Description
```
Performs a multi-byte safe (UTF-8) conversion of all chars in string to lower case.
```

#### Note
```
Although most code points can be converted in-place, there are notable
exceptions and the final length can vary.
```

#### Note
```
Case mapping is not reversible. That is, toUpper(toLower(x)) != toLower(toUpper(x)).
```

#### Return
```
Number of bytes written.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

