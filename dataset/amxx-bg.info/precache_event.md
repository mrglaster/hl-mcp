# precache_event
#### Syntax
```
native precache_event(type, const Name[], any:...);
```

#### Usage
type | ```Event type```
---|---
Name | ```Formatting rules, path to the event file```
... | ```Variable number of formatting parameters```
#### Description
```
Precaches an event file.
```

#### Note
```
The event type should always be 1.
```

#### Note
```
Contrary to the other precache_* natives, this can be used outside of
the plugin_precache() forward, e.g. in plugin_init() or plugin_cfg().
A bug in some clients makes this necessary, as plugin_precache() is
called before the mod has precached its own, default event files. This
can cause the event table to be misaligned on the client, leading to
visual and audio bugs that are hard to diagnose.
```

#### Return
```
Unique cache id of the event
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

