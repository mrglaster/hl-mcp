# regex_compile
#### Syntax
```
native Regex:regex_compile(const pattern[], &ret = 0, error[] = "", maxLen = 0, const flags[]="");
```

#### Usage
pattern | ```The regular expression pattern.```
---|---
ret | ```Error code encountered, if applicable.```
error | ```Error message encountered, if applicable.```
maxLen | ```Maximum string length of the error buffer.```
flags | ```General flags for the regular expression. i = Ignore case m = Multilines (affects ^ and $ so that they match     the start/end of a line rather than matching the     start/end of the string). s = Single line (affects . so that it matches any character,     even new line characters). x = Pattern extension (ignore whitespace and # comments).```
#### Description
```
Precompile a regular expression.
```

#### Note
```
Use this if you intend on using the same expression multiple times.
Pass the regex handle returned here to regex_match_c to check for matches.
```

#### Note
```
This handle is automatically freed on map change.  However,
if you are completely done with it before then, you should
call regex_free on this handle.
```

#### Note
```
Consider using regex_compile_ex instead if you want to use PCRE_* flags.
```

#### Return
```
-1 on error in the pattern, > valid regex handle (> 0) on success.
```


This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

