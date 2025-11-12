# plugin_precache
#### Syntax
```
forward plugin_precache();
```

#### Description
```
This forward allows plugins to add models, sounds and generic files to the
precache tables using the precache_* set of functions.
```

#### Note
```
Adding files to the precaching tables will trigger the client to
download them to its local filesystem.
```

#### Note
```
There is a hard upper limit of entries in the precaching tables for
every game, this limit is 512 in most cases. The entries will be filled
and indexed incrementally. Going over this limit will crash the server.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

