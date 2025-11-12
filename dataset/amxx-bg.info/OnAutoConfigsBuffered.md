# OnAutoConfigsBuffered
#### Syntax
```
forward OnAutoConfigsBuffered();
```

#### Description
```
Called when the map has loaded, right after plugin_cfg() but any time
before OnConfigsExecuted.  It's called after amxx.cfg and  all
AutoExecConfig() exec commands have been added to the server command buffer.
```

#### Note
```
This will always be called once and only once per map.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

