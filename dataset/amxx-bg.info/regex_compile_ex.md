# regex_compile_ex
#### Syntax
```
native Regex:regex_compile_ex(const pattern[], flags = 0, error[]= "", maxLen = 0, &errcode = 0);
```

#### Usage
pattern | ```The regular expression pattern.```
---|---
flags | ```General flags for the regular expression, see PCRE_* defines.```
error | ```Error message encountered, if applicable.```
maxLen | ```Maximum string length of the error buffer.```
errcode | ```Regex type error code encountered, if applicable. See REGEX_ERROR_* defines.```
#### Description
```
Precompile a regular expression.
```

#### Note
```
Use this if you intend on using the same expression multiple times.
Pass the regex handle returned here to regex_match_c() to check for matches.
```

#### Note
```
Unlike regex_compile(), this allows you to use PCRE flags directly.
```

#### Return
```
Valid regex handle (> 0) on success, or -1 on failure.
```


This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

