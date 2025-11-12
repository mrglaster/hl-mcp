# vdformat
#### Syntax
```
native vdformat(buffer[], len, fmt_arg, vararg, ...);
```

#### Usage
buffer | ```Destination string buffer.```
---|---
len | ```Maximum length of output string buffer.```
fmt_arg | ```Argument number which contains the format.```
vararg | ```Argument number which contains the '...' symbol. Note: Arguments start at 1.```
#### Description
```
Formats a string according to the AMX Mod X format rules (see documentation).
```

#### Note
```
Same as vformat(), except works in normal style dynamic natives.
Instead of passing the format arg string, you can only pass the
actual format argument number itself.
If you pass 0, it will read the format string from an optional
fifth parameter.
```

#### Return
```
Number of bytes written.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

