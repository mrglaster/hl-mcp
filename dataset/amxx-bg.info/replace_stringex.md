# replace_stringex
#### Syntax
```
native replace_stringex(text[], maxlength, const search[], const replace[], searchLen = -1, replaceLen = -1, bool:caseSensitive = true);
```

#### Usage
text | ```String to perform search and replacements on.```
---|---
maxlength | ```Maximum length of the string buffer.```
search | ```String to search for.```
replace | ```String to replace the search string with.```
searchLen | ```If higher than -1, its value will be used instead of a strlen() call on the search parameter.```
replaceLen | ```If higher than -1, its value will be used instead of a strlen() call on the replace parameter.```
caseSensitive | ```If true (default), search is case sensitive.```
#### Description
```
Given a string, replaces the first occurrence of a search string with a
replacement string.
```

#### Note
```
Similar to replace() native, but implemented with more options and
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
Index into the buffer (relative to the start) from where
the last replacement ended, or -1 if no replacements were
made.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

