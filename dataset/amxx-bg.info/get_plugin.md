# get_plugin
#### Syntax
```
native get_plugin(index, filename[] = "", len1 = 0, name[] = "", len2 = 0, version[] = "", len3 = 0, author[] = "", len4 = 0, status[] = "", len5 = 0, url[] = "", len6 = 0, desc[] = "", len7 = 0);
```

#### Usage
index | ```Plugin index, -1 to target calling plugin```
---|---
filename | ```Buffer to copy plugin filename to```
len1 | ```Maximum filename buffer size```
name | ```Buffer to copy plugin name to```
len2 | ```Maximum name buffer size```
version | ```Buffer to copy plugin version to```
len3 | ```Maximum version buffer size```
author | ```Buffer to copy plugin author to```
len4 | ```Maximum author buffer size```
status | ```Buffer to copy plugin status flags to```
len5 | ```Maximum status buffer size```
url | ```Buffer to copy plugin url to```
len6 | ```Maximum url buffer size```
desc | ```Buffer to copy plugin description to```
len7 | ```Maximum description buffer size```
#### Description
```
Retrieves info about a plugin by plugin index.
```

#### Return
```
Plugin index on success, -1 if there is no plugin with given
index
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

