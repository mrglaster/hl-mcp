# strtof
#### Syntax
```
native Float:strtof(const string[], &endPos = 0);
```

#### Usage
string | ```The string to parse.```
---|---
endPos | ```The position of the first character following the number. On success and when containing only numbers, position is at the end of string, meaning equal to 'string' length. On failure, position is sets always to 0.```
#### Description
```
Parses the 'string' interpreting its content as an floating point number and returns its value as a float.
The function also sets the value of 'endPos' to point to the position of the first character after the number.

This is the same as C++ strtod function with a difference on second param.

The function first discards as many whitespace characters as necessary until the first
non-whitespace character is found. Then, starting from this character, takes as many
characters as possible that are valid and interprets them as a numerical value.
Finally, a position of the first character following the float representation in 'string'
is stored in 'endPos'.

If the first sequence of non-whitespace characters in 'string' is not a valid float number
as defined above, or if no such sequence exists because either 'string' is empty or it contains
only whitespace characters, no conversion is performed.
```

#### Return
```
On success, the function returns the converted floating point number as float value.
If no valid conversion could be performed, a zero value is returned.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

