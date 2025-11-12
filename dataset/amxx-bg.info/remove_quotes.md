# remove_quotes
#### Syntax
```
native remove_quotes(text[]);
```

#### Usage
text | ```String to remove double-quotes from```
---|---
#### Description
```
Removes double-quotes from the beginning and end of a string.
```

#### Note
```
If the string only has a double-quote at either the start *or* the end,
and not both, the function will do nothing.
```

#### Note
```
The function does not perform any trimming per-se. But if a
double-quote is found at the beginning of the string, it will remove
one ^r (carriage return) character at the end of the string if present,
even if no matching double-quote is found. This is for convenience.
```

#### Return
```
1 if matching double-quotes have been removed, 0 otherwise
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

