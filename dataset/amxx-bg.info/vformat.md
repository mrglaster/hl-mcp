# vformat
#### Syntax
```
native vformat(buffer[], len, const fmt[], vararg);
```

#### Usage
buffer | ```Destination string buffer.```
---|---
len | ```Maximum length of output string buffer.```
fmt | ```Formatting rules.```
vararg | ```Argument number which contains the '...' symbol. Note: Arguments start at 1.```
#### Description
```
Formats a string according to the AMX Mod X format rules (see documentation).
```

#### Note
```
This is the same as format(), except it grabs parameters from a
parent parameter stack, rather than a local.  This is useful for
implementing your own variable argument functions.
```

#### Note
```
Replacement for format_args.  Much faster and %L compatible.
This works exactly like vsnprintf() from C.
You must pass in the output buffer and its size,
 the string to format, and the number of the FIRST variable
 argument parameter.  For example, for:
 function (a, b, c, ...)
 You would pass 4 (a is 1, b is 2, c is 3, et cetera).
There is no vformatex().
```

#### Return
```
Number of bytes written.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

