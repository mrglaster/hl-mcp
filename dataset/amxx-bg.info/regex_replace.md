# regex_replace
#### Syntax
```
native regex_replace(Regex:pattern, string[], maxLen, const replace[], flags = REGEX_FORMAT_DEFAULT, &errcode = 0);
```

#### Usage
pattern | ```The regular expression pattern.```
---|---
string | ```The string to check.```
error | ```Error message, if applicable.```
maxLen | ```Maximum length of the error buffer.```
replace | ```The string will be used to replace any matches. See above for format specifiers.```
flags | ```General flags to control how the string is replaced. See REGEX_FORMAT_* defines.```
errcode | ```Regex type error code encountered, if applicable. See REGEX_ERROR_* defines.```
#### Description
```
Perform a regular expression search and replace.

An optional parameter, flags, allows you to specify options on how the replacement is performed.
Supported format specifiers for replace parameter:
  $number  : Substitutes the substring matched by group number.
             n must be an integer value designating a valid backreference, greater than 0, and of two digits at most.
  ${name}  : Substitutes the substring matched by the named group name (a maximum of 32 characters).
  $&       : Substitutes a copy of the whole match.
  $`       : Substitutes all the text of the input string before the match.
  $'       : Substitutes all the text of the input string after the match.
  $+       : Substitutes the last group that was captured.
  $_       : Substitutes the entire input string.
  $$       : Substitutes a literal "$".
As note, the character \ can be also used with format specifier, this is same hehavior as $.
```

#### Return
```
-2 = Matching error (error code is stored in ret)
 0 = No match.
>1 = Number of matches.
```


This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

