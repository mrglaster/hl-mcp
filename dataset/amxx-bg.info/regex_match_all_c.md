# regex_match_all_c
#### Syntax
```
native regex_match_all_c(const string[], Regex:pattern, &ret = 0);
```

#### Usage
pattern | ```The regular expression pattern.```
---|---
string | ```The string to check.```
ret | ```Error code, if applicable, or number of results on success. See REGEX_ERROR_* defines.```
#### Description
```
Matches a string against a pre-compiled regular expression pattern, matching all
occurrences of the pattern inside the string. This is similar to using the "g" flag
in perl regex.
```

#### Note
```
You should free the returned handle (with regex_free())
when you are done with this pattern.
```

#### Note
```
Use the regex handle passed to this function to extract
matches with regex_substr().
```

#### Return
```
-2 = Matching error (error code is stored in ret)
 0 = No match.
>1 = Number of results.
```


This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

