# regex_free
#### Syntax
```
native regex_free(&Regex:id);
```

#### Usage
id | ```The regex handle to free.```
---|---
#### Description
```
Frees the memory associated with a regex result, and sets the handle to 0.
```

#### Note
```
This must be called on all results from regex_match() when you are done extracting
the results with regex_substr().
```

#### Note
```
The results of regex_compile() or regex_compile_ex() (and subsequently, regex_match_c())
only need to be freed when you are done using the pattern.
```

#### Note
```
Do not use the handle again after freeing it!
```

#### Return
```
This function has no return value.
```


This code is a part of regex.inc. To use this code you should include regex.inc as ```#include <regex>```


  
  

