# regex_match_all
#### Syntax
```
native Regex:regex_match_all(const string[], const pattern[], flags = 0, error[]= "", maxLen = 0, &errcode = 0);
```

#### Usage
string | ```The string to check.```
---|---
pattern | ```The regular expression pattern.```
flags | ```General flags for the regular expression, see PCRE_* defines.```
error | ```Error message encountered, if applicable.```
maxLen | ```Maximum string length of the error buffer.```
errcode | ```Regex type error code encountered, if applicable. See REGEX_ERROR_* defines.```
#### Description
```
Matches a string against a regular expression pattern, matching all occurrences of the
pattern inside the string. This is similar to using the "g" flag in perl regex.
```

#### Note
```
If you intend on using the same regular expression pattern
multiple times, consider using regex_compile and regex_match_ex
instead of making this function reparse the expression each time.
```

#### Note
```
Flags only exist in amxmodx 1.8 and later.
```

#### Note
```
You should free the returned handle with regex_free()
when you are done extracting all of the substrings.
```

#### Return
```
-2 = Matching error (error code is stored in ret)
-1 = Error in pattern (error message and offset # in error and ret)
 0 = No match.
>1 = Handle for getting more information (via regex_substr)
```


This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

