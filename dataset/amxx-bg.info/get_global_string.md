# get_global_string
#### Syntax
```
native get_global_string(variable, string[], maxlen);
```

#### Usage
variable | ```Entry to retrieve from```
---|---
string | ```Buffer to copy value to```
maxlen | ```Maximum size of buffer```
#### Description
```
Retrieves a global string type value from the server.
```

#### Note
```
For a list of valid string type entries, see the GL_* constants in
engine_const.inc under the "String" section.
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If an invalid entry is provided, an error will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

