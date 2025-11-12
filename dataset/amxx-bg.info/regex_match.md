# regex_match
#### Syntax
```
native Regex:regex_match(const string[], const pattern[], &ret = 0, error[] = "", maxLen = 0, const flags[] = "");
```

#### Usage
string | ```The string to check.```
---|---
pattern | ```The regular expression pattern.```
ret | ```Error code, or result state of the match.```
error | ```Error message, if applicable.```
maxLen | ```Maximum length of the error buffer.```
flags | ```General flags for the regular expression. i = Ignore case m = Multilines (affects ^ and $ so that they match     the start/end of a line rather than matching the     start/end of the string). s = Single line (affects . so that it matches any character,     even new line characters). x = Pattern extension (ignore whitespace and # comments).```
#### Description
```
Matches a string against a regular expression pattern.
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


  
  

