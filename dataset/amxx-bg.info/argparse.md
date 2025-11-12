# argparse
#### Syntax
```
native argparse(const text[], pos, argbuffer[], maxlen);
```

#### Usage
text | ```String to tokenize.```
---|---
pos | ```Position to start parsing from.```
argbuffer | ```Buffer to store first argument.```
maxlen | ```Size of the buffer.```
#### Description
```
Parses an argument string to find the first argument. You can use this to
replace strbreak().
```

#### Note
```
Only available in 1.8.3 and above.
```

#### Note
```
You can use argparse() to break a string into all of its arguments:
new arg[N], pos;
while (true) {
  pos = argparse(string, pos, arg, sizeof(arg) - 1);
  if (pos == -1)
    break;
}
```

#### Note
```
All initial whitespace is removed. Remaining characters are read until an
argument separator is encountered. A separator is any whitespace not inside
a double-quotation pair (i.e. "x b" is one argument). If only one quotation
mark appears, argparse() acts as if one existed at the end of the string.
Quotation marks are never written back, and do not act as separators. For
example, "a""b""c" will return "abc". An empty quote pair ("") will count
as an argument containing no characters.
```

#### Note
```
argparse() will write an empty string to argbuffer if no argument is found.
```

#### Return
```
If no argument was found, -1 is returned. Otherwise,
the index to the next position to parse from is
returned. This might be the very end of the string.
```


This code is a part of string.inc. To use this code you should include string.inc as ```#include <string>```


  
  

