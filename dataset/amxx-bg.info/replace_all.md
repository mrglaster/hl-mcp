# replace_all
#### Syntax
```
stock replace_all(string[], len, const what[], const with[])
```

#### Usage
string | ```String to perform search and replacements on.```
---|---
len | ```Maximum length of the string buffer.```
what | ```String to search for.```
with | ```String to replace the search string with.```
#### Description
```
Replaces a contained string iteratively.
```

#### Note
```
Consider using replace_string() instead.
```

#### Note
```
This ensures that no infinite replacements will take place by
intelligently moving to the next string position each iteration.
```

#### Return
```
Number of replacements on success, otherwise 0.
```


This code is a part of string_stocks.inc. To use this code you should include string_stocks.inc as ```#include <string_stocks>```


  
  

