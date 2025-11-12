# get_func_id
#### Syntax
```
native get_func_id(const funcName[], pluginId = -1);
```

#### Usage
funcName | ```Function name```
---|---
pluginId | ```Plugin id, if -1 the calling plugin is targeted The plugin id can be retrieved using find_plugin_byfile()```
#### Description
```
Retrieves a functions id for use with callfunc_begin_i()
```

#### Return
```
>=0 Function id on success
-1 if plugin or function was not found
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

