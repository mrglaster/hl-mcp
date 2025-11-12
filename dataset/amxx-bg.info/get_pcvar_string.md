# get_pcvar_string
#### Syntax
```
native get_pcvar_string(pcvar, string[], maxlen);
```

#### Usage
pcvar | ```Pointer to cvar to retrieve value from```
---|---
string | ```Buffer to copy cvar value to```
maxlen | ```Maximum size of the buffer```
#### Description
```
Returns a string value from a cvar via direct pointer access.
```

#### Return
```
Number of cells written to buffer.
```

#### Error
```
If an invalid cvar pointer is provided, an error will be
thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

