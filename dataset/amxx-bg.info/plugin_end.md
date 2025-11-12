# plugin_end
#### Syntax
```
forward plugin_end();
```

#### Description
```
Called just before server deactivation and subsequent unloading of the
plugin.
```

#### Note
```
The plugin is required to manually free Handles it has acquired, such
as those from dynamic data structures. Failing to do that will result
in the plugin and AMXX leaking memory.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

