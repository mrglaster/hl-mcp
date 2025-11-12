# is_plugin_loaded
#### Syntax
```
native is_plugin_loaded(const name[], bool:usefilename = false);
```

#### Usage
name | ```Plugin name or filename```
---|---
usefilename | ```If true searches for plugin filename, false searches for plugin name```
#### Description
```
Returns if a plugin is loaded by registered name or filename.
```

#### Note
```
An example for a registered name would be "Admin Base", while a possible
filename would be "admin.amxx".
```

#### Note
```
Prior to AMXX 1.80, this function would only search for plugins
registered names, not the filename.
```

#### Note
```
The plugin name matching is case insensitive, while the filename
matching is case sensitive.
```

#### Return
```
Plugin id of the matching plugin, -1 otherwise
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

