# ns_get_gameplay
#### Syntax
```
native NSGameplay:ns_get_gameplay();
```

#### Description
```
Returns the gameplay type for the currently active map.
Refer to ns_const.inc's NSGameplay enum for details.
```

#### Note
```
The earliest this is guaranteed to be accurate is during plugin_init().  It needs
the info_gameplay entity to be properly set within the map, or it will return "Unknown",
or "Cantfind".
```

#### Return
```
Return the gameplay mode, as accurate as the module can tell.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).