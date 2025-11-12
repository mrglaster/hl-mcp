# CreateOneForward
#### Syntax
```
native CreateOneForward(plugin_id, const name[], ...);
```

#### Usage
plugin_id | ```Plugin to call forward in. The plugin id can be retrieved using find_plugin_byfile()```
---|---
name | ```Function name to call```
... | ```List of parameter types```
#### Description
```
Creates a private forward that will be called in a single plugin.
```

#### Note
```
Unlike other natives expecting a plugin id, specifying -1 will not
select the calling plugin, and instead throw an error.
```

#### Return
```
Forward handle, -1 on failure
```

#### Error
```
If an invalid plugin id is specified, an error will be
thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

