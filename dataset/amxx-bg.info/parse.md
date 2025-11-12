# parse
#### Syntax
```
native parse(const text[], ... );
```

#### Usage
text | ```String to parse.```
---|---
... | ```Variable number of format parameters.```
#### Description
```
Gets parameters from text.
```

#### Note
```
Example: to split text: "^"This is^" the best year",
call function like this: parse(text,arg1,len1,arg2,len2,arg3,len3,arg4,len4)
and you will get: "This is", "the", "best", "year"
Function returns number of parsed parameters.
```

#### Return
```
Number of parsed parameters.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

