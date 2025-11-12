# Functions in string.inc
Function | Description  
---|---  
[strlen](https://amxx-bg.info/api/string/strlen) | ```
Calculates the length of a string.
```
  
[contain](https://amxx-bg.info/api/string/contain) | ```
Tests whether a string is found inside another string.
```
  
[containi](https://amxx-bg.info/api/string/containi) | ```
Tests whether a string is found inside another string with case ignoring.
```
  
[replace](https://amxx-bg.info/api/string/replace) | ```
Given a string, replaces the first occurrence of a search string with a
replacement string.
```
  
[replace_string](https://amxx-bg.info/api/string/replace_string) | ```
Given a string, replaces all occurrences of a search string with a
replacement string.
```
  
[replace_stringex](https://amxx-bg.info/api/string/replace_stringex) | ```
Given a string, replaces the first occurrence of a search string with a
replacement string.
```
  
[add](https://amxx-bg.info/api/string/add) | ```
Concatenates one string onto another.
```
  
[format](https://amxx-bg.info/api/string/format) | ```
Formats a string according to the AMX Mod X format rules (see documentation).
```
  
[formatex](https://amxx-bg.info/api/string/formatex) | ```
Formats a string according to the AMX Mod X format rules (see documentation).
```
  
[[MAX_FMT_LENGTH]fmt](https://amxx-bg.info/api/string/\[MAX_FMT_LENGTH\]fmt) | ```
Formats and returns a string according to the AMX Mod X format rules
(see documentation).
```
  
[vformat](https://amxx-bg.info/api/string/vformat) | ```
Formats a string according to the AMX Mod X format rules (see documentation).
```
  
[vdformat](https://amxx-bg.info/api/string/vdformat) | ```
Formats a string according to the AMX Mod X format rules (see documentation).
```
  
[format_args](https://amxx-bg.info/api/string/format_args) | ```
Gets parameters from function as formated string.
```
  
[num_to_str](https://amxx-bg.info/api/string/num_to_str) | ```
Converts an integer to a string.
```
  
[str_to_num](https://amxx-bg.info/api/string/str_to_num) | ```
Converts a string to an integer.
```
  
[strtol](https://amxx-bg.info/api/string/strtol) | ```
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
  
[strtof](https://amxx-bg.info/api/string/strtof) | ```
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
  
[float_to_str](https://amxx-bg.info/api/string/float_to_str) | ```
Converts a floating point number to a string.
```
  
[str_to_float](https://amxx-bg.info/api/string/str_to_float) | ```
Converts a string to a floating point number.
```
  
[equal](https://amxx-bg.info/api/string/equal) | ```
Returns whether two strings are equal.
```
  
[equali](https://amxx-bg.info/api/string/equali) | ```
Returns whether two strings are equal with case ignoring.
```
  
[copy](https://amxx-bg.info/api/string/copy) | ```
Copies one string to another string.
```
  
[copyc](https://amxx-bg.info/api/string/copyc) | ```
Copies one string to another string until ch is found.
```
  
[setc](https://amxx-bg.info/api/string/setc) | ```
Sets string with given character.
```
  
[parse](https://amxx-bg.info/api/string/parse) | ```
Gets parameters from text.
```
  
[strtok](https://amxx-bg.info/api/string/strtok) | ```
Breaks a string in two by token.
```
  
[strtok2](https://amxx-bg.info/api/string/strtok2) | ```
Breaks a string in two by token.
```
  
[trim](https://amxx-bg.info/api/string/trim) | ```
Removes whitespace characters from the beginning and end of a string.
```
  
[strtolower](https://amxx-bg.info/api/string/strtolower) | ```
Converts all chars in string to lower case.
```
  
[mb_strtolower](https://amxx-bg.info/api/string/mb_strtolower) | ```
Performs a multi-byte safe (UTF-8) conversion of all chars in string to lower case.
```
  
[strtoupper](https://amxx-bg.info/api/string/strtoupper) | ```
Converts all chars in string to upper case.
```
  
[mb_strtoupper](https://amxx-bg.info/api/string/mb_strtoupper) | ```
Performs a multi-byte safe (UTF-8) conversion of all chars in string to upper case.
```
  
[ucfirst](https://amxx-bg.info/api/string/ucfirst) | ```
Make a string's first character uppercase.
```
  
[mb_ucfirst](https://amxx-bg.info/api/string/mb_ucfirst) | ```
Performs a multi-byte safe (UTF-8) conversion of a string's first character to upper case.
```
  
[mb_strtotitle](https://amxx-bg.info/api/string/mb_strtotitle) | ```
Performs a multi-byte safe (UTF-8) conversion of all chars in string to title case.
```
  
[is_string_category](https://amxx-bg.info/api/string/is_string_category) | ```
Checks if the input string conforms to the category specified by the flags.
```
  
[isdigit](https://amxx-bg.info/api/string/isdigit) | ```
Returns whether a character is numeric.
```
  
[isalpha](https://amxx-bg.info/api/string/isalpha) | ```
Returns whether a character is an ASCII alphabet character.
```
  
[isspace](https://amxx-bg.info/api/string/isspace) | ```
Returns whether a character is whitespace.
```
  
[isalnum](https://amxx-bg.info/api/string/isalnum) | ```
Returns whether a character is numeric or an ASCII alphabet character.
```
  
[is_char_mb](https://amxx-bg.info/api/string/is_char_mb) | ```
Returns if a character is multi-byte or not.
```
  
[is_char_upper](https://amxx-bg.info/api/string/is_char_upper) | ```
Returns whether an alphabetic character is uppercase.
```
  
[is_char_lower](https://amxx-bg.info/api/string/is_char_lower) | ```
Returns whether an alphabetic character is lowercase.
```
  
[get_char_bytes](https://amxx-bg.info/api/string/get_char_bytes) | ```
Returns the number of bytes a character is using.  This is
for multi-byte characters (UTF-8).  For normal ASCII characters,
this will return 1.
```
  
[strcat](https://amxx-bg.info/api/string/strcat) | ```
Concatenates one string onto another.
```
  
[strfind](https://amxx-bg.info/api/string/strfind) | ```
Tests whether a string is found inside another string.
```
  
[strcmp](https://amxx-bg.info/api/string/strcmp) | ```
Compares two strings lexographically.
```
  
[strncmp](https://amxx-bg.info/api/string/strncmp) | ```
Compares two strings parts lexographically.
```
  
[argparse](https://amxx-bg.info/api/string/argparse) | ```
Parses an argument string to find the first argument. You can use this to
replace strbreak().
```
  
[split_string](https://amxx-bg.info/api/string/split_string) | ```
Returns text in a string up until a certain character sequence is reached.
```
  

This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

