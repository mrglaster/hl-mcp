# precache_generic
#### Syntax
```
native precache_generic(const szFile[]);
```

#### Usage
szFile | ```Path to the file```
---|---
#### Description
```
Precaches a generic file.
```

#### Note
```
Can only be used inside of the plugin_precache() forward.
```

#### Note
```
Precaching sounds with this will not add them to the engine sound table.
```

#### Return
```
Unique cache id of the file
```

#### Error
```
If called outside of the plugin_precache() forward, an error
is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

