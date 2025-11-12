# copy_keyvalue
#### Syntax
```
native copy_keyvalue(szClassName[], sizea, szKeyName[], sizeb, szValue[], sizec);
```

#### Usage
szClassName | ```Buffer to copy classname to```
---|---
sizea | ```Maximum size of classname buffer```
szKeyName | ```Buffer to copy keyname to```
sizeb | ```Maximum size of keyname buffer```
szVlaue | ```Buffer to copy value to```
sizec | ```Maximum size of value buffer```
#### Description
```
Retrieves buffers from the keyvalue structure.
```

#### Note
```
Can only be used inside the pfn_keyvalue() forward.
```

#### Return
```
1 on success, 0 if used outside the pfn_keyvalue()
forward
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

