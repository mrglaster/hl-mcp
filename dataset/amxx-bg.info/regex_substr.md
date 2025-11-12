# regex_substr
#### Syntax
```
native regex_substr(Regex:id, str_id, buffer[], maxLen);
```

#### Usage
id | ```The regex handle to extract data from.```
---|---
str_id | ```The index of the expression to get - starts at 0, and ends at ret - 1.```
buffer | ```The buffer to set to the matching substring.```
maxLen | ```The maximum string length of the buffer.```
#### Description
```
Returns a matched substring from a regex handle.
```

#### Note
```
Substring ids start at 0 and end at ret - 1, where ret is from the corresponding
regex_match* function call.
```

#### Return
```
1 on success, otherwise 0 on failure.
```


This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

