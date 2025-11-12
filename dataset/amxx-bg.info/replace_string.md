# replace_string
#### Syntax
```
native replace_string(text[], maxlength, const search[], const replace[], bool:caseSensitive = true);
```

#### Usage
text | ```String to perform search and replacements on.```
---|---
maxlength | ```Maximum length of the string buffer.```
search | ```String to search for.```
replace | ```String to replace the search string with.```
caseSensitive | ```If true (default), search is case sensitive.```
#### Description
```
Given a string, replaces all occurrences of a search string with a
replacement string.
```

#### Note
```
Similar to replace_all() stock, but implemented as native and
with different algorithm. This native doesn't error on bad
buffer size and will smartly cut off the string in a way
that pushes old data out.
```

#### Note
```
Only available in 1.8.3 and above.
```

#### Note
```
This supports multi-byte characters (UTF-8) on case insensitive comparison.
```

#### Return
```
Number of replacements that were performed.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

