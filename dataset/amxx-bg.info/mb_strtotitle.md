# mb_strtotitle
#### Syntax
```
native mb_strtotitle(string[], maxlength = 0);
```

#### Usage
string | ```The string to convert.```
---|---
maxlength | ```Optional size of the buffer. If 0, the length of the original string will be used instead.```
#### Description
```
Performs a multi-byte safe (UTF-8) conversion of all chars in string to title case.
```

#### Note
```
Although most code points can be converted in-place, there are notable
exceptions and the final length can vary.
```

#### Note
```
Any type of punctuation can break up a word, even if this is
not grammatically valid. This happens because the titlecasing algorithm
does not and cannot take grammar rules into account.
```

#### Note
```
Examples:
  The running man                      | The Running Man
  NATO Alliance                        | Nato Alliance
  You're amazing at building libraries | You'Re Amazing At Building Libraries
```

#### Return
```
Number of bytes written.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

