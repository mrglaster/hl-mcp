# strtol
#### Syntax
```
native strtol(const string[], &endPos = 0, base = 0);
```

#### Usage
string | ```The string to parse.```
---|---
endPos | ```The position of the first character following the number. On success and when containing only numbers, position is at the end of string, meaning equal to 'string' length. On failure, position is sets always to 0.```
base | ```The numerical base (radix) that determines the valid characters and their interpretation. If this is 0, the base used is determined by the format in the sequence.```
#### Description
```
Parses the 'string' interpreting its content as an integral number of the specified 'base',
which is returned as integer value. The function also sets the value of 'endPos' to point
to the position of the first character after the number.

This is the same as C++ strtol function with a difference on second param.

The function first discards as many whitespace characters as necessary until the first
non-whitespace character is found. Then, starting from this character, takes as many
characters as possible that are valid following a syntax that depends on the 'base' parameter,
and interprets them as a numerical value. Finally, a position of the first character following
the integer representation in 'string' is stored in 'endPos'.

If the value of 'base' is zero, the syntax expected is similar to that of integer constants,
which is formed by a succession of :
   An optional sign character (+ or -)
   An optional prefix indicating octal or hexadecimal base ("0" or "0x"/"0X" respectively)
   A sequence of decimal digits (if no base prefix was specified) or either octal or hexadecimal digits if a specific prefix is present

If the 'base' value is between 2 and 36, the format expected for the integral number is a succession
of any of the valid digits and/or letters needed to represent integers of the specified radix
(starting from '0' and up to 'z'/'Z' for radix 36). The sequence may optionally be preceded by
a sign (either + or -) and, if base is 16, an optional "0x" or "0X" prefix.

If the first sequence of non-whitespace characters in 'string' is not a valid integral number
as defined above, or if no such sequence exists because either 'string' is empty or it contains
only whitespace characters, no conversion is performed.
```

#### Return
```
On success, the function returns the converted integral number as integer value.
If no valid conversion could be performed, a zero value is returned.
If the value read is out of the range of representable values by a cell,
the function returns 'cellmin' or 'cellmax'.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

