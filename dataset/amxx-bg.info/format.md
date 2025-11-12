# format
#### Syntax
```
native format(output[], len, const format[], any:...);
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
Example: format(dest, "Hello %s. You are %d years old", "Tom", 17).
If any of your input buffers overlap with the destination buffer,
format() falls back to a "copy-back" version as of 1.65.  This is
slower, so you should using a source string that is the same as
the destination.
```

#### Return
```
Number of cells written.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

