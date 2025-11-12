# formatex
#### Syntax
```
native formatex(output[], len, const format[], any:...);
```

#### Usage
output | ```Destination string buffer.```
---|---
len | ```Maximum length of output string buffer.```
format | ```Formatting rules.```
... | ```Variable number of format parameters.```
#### Description
```
Formats a string according to the AMX Mod X format rules (see documentation).
```

#### Note
```
Same as format(), except does not perform a "copy back" check.
This means formatex() is faster, but DOES NOT ALLOW this type
of call:
  formatex(buffer, len, "%s", buffer)
  formatex(buffer, len, buffer, buffer)
  formatex(buffer, len, "%s", buffer[5])
This is because the output is directly stored into "buffer",
rather than copied back at the end.
```

#### Return
```
Number of cells written.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

