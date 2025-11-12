# explode_string
#### Syntax
```
stock explode_string(const text[], const split[], buffers[][], maxStrings, maxStringLength, bool:copyRemainder = false)
```

#### Usage
text | ```The string to split.```
---|---
split | ```The string to use as a split delimiter.```
buffers | ```An array of string buffers (2D array).```
maxStrings | ```Number of string buffers (first dimension size).```
maxStringLength | ```Maximum length of each string buffer.```
copyRemainder | ```False (default) discard excess pieces, true to ignore delimiters after last piece.```
#### Description
```
Breaks a string into pieces and stores each piece into an array of buffers.
```

#### Return
```
Number of strings retrieved.
```


This code is a part of string_stocks.inc. To use this code you should include string_stocks.inc as ```#include <string_stocks>```


  
  

