# pfn_keyvalue
#### Syntax
```
forward pfn_keyvalue(entid);
```

#### Usage
entid | ```Entity index```
---|---
#### Description
```
Called when a keyvalue pair is sent to an entity.
```

#### Note
```
Use copy_keyvalue() to retrieve the keyvalue information, and
DispatchKeyVaue() to modify it.
```

#### Return
```
PLUGIN_CONTINUE to ignore, PLUGIN_HANDLED or higher to block
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

