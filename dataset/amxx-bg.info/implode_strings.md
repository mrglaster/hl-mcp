# implode_strings
#### Syntax
```
stock implode_strings(const strings[][], numStrings, const join[], buffer[], maxLength)
```

#### Usage
strings | ```An array of strings.```
---|---
numStrings | ```Number of strings in the array.```
join | ```The join string to insert between each string.```
buffer | ```Output buffer to write the joined string to.```
maxLength | ```Maximum length of the output buffer.```
#### Description
```
Joins an array of strings into one string, with a "join" string inserted in
between each given string.  This function complements ExplodeString.
```

#### Return
```
Number of bytes written to the output buffer.
```


This code is a part of string_stocks.inc. To use this code you should include string_stocks.inc as ```#include <string_stocks>```


  
  

