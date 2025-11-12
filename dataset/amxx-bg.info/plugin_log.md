# plugin_log
#### Syntax
```
forward plugin_log();
```

#### Description
```
Called when a message is about to be logged.
```

#### Note
```
Message data and information can be retrieved using the read_log* set
of functions.
```

#### Return
```
PLUGIN_CONTINUE to let the log message through
PLUGIN_HANDLED or higher to stop the log message
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

