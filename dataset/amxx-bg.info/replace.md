# replace
#### Syntax
```
native replace(text[], len, const what[], const with[]);
```

#### Usage
text | ```String to perform search and replacements on.```
---|---
len | ```Maximum length of the string buffer.```
what | ```String to search for.```
with | ```String to replace the search string with.```
#### Description
```
Given a string, replaces the first occurrence of a search string with a
replacement string.
```

#### Return
```
The new string length after replacement, or 0 if no replacements were made.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

