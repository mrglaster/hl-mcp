# OnConfigsExecuted
#### Syntax
```
forward OnConfigsExecuted();
```

#### Description
```
Called when the map has loaded, and all configs are done executing.
This includes servercfgfile (server.cfg), amxx.cfg, plugin's config, and
per-map config.
```

#### Note
```
This is best place to initialize plugin functions which are based on cvar data.
```

#### Note
```
This will always be called once and only once per map.  It will be
called few seconds after plugin_cfg().
```

#### Return
```
This forward ignores the return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

