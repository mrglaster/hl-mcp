# regex_match_simple
#### Syntax
```
stock regex_match_simple(const str[], const pattern[], flags = 0, error[]= "", maxLen = 0, &errcode = 0)
```

#### Usage
str | ```The string to check.```
---|---
pattern | ```The regular expression pattern.```
flags | ```General flags for the regular expression.```
error | ```Error message, if applicable.```
maxLen | ```Maximum length of the error buffer.```
errcode | ```Regex type error code encountered, if applicable. See REGEX_ERROR_* defines.```
#### Description
```
Matches a string against a regular expression pattern.
```

#### Note
```
If you intend on using the same regular expression pattern
multiple times, consider using compile regex_compile_ex and regex_match*
instead of making this function reparse the expression each time.
```

#### Return
```
-2 = Matching error (error code is stored in ret)
-1 = Pattern error (error code is stored in ret)
 0 = No match.
>1 = Number of results.
```


This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

