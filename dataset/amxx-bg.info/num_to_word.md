# num_to_word
#### Syntax
```
native num_to_word(num, output[], len);
```

#### Usage
num | ```Integer to convert```
---|---
output | ```Buffer to copy string to```
len | ```Maximum buffer size```
#### Description
```
Converts an integer to a text string.
```

#### Note
```
The conversion algorithm is limited to a certain range of numbers, but
is guaranteed to work correctly for all numbers from 0 to 999. Outside
of that range, the conversion will result in an incorrect string, but
will not fail.
```

#### Note
```
The conversion is to english text, there is no way to change this.
```

#### Return
```
Number of cells written to buffer
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

