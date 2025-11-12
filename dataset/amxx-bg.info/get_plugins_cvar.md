# get_plugins_cvar
#### Syntax
```
native get_plugins_cvar(num, name[], namelen, &flags = 0, &plugin_id = 0, &pcvar_handle = 0, description[] = "", desc_len = 0);
```

#### Usage
num | ```Index to retrieve```
---|---
name | ```Buffer to copy cvar name to```
namelen | ```Maximum buffer size```
flags | ```Variable to store cvar flags to```
plugin_id | ```Variable to store id of the registering plugin to```
pcvar_handle | ```Variable to store cvar pointer to```
description | ```Variable to store cvar description to```
desc_len | ```Maximum length of string buffer```
#### Description
```
Retrieves information about a plugin-registered cvar via iterative access.
```

#### Note
```
The returned cvar pointer should be used with the get_pcvar_* and
set_pcvar_* set of functions.
```

#### Note
```
The cvar index does not equal the cvar pointer. It is the internal
AMXX id of a cvar, incremented for each registered cvar.
```

#### Return
```
1 on success, 0 if index is invalid
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

