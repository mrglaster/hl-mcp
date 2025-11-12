# DispatchKeyValue
#### Syntax
```
native DispatchKeyValue(...);
```

#### Usage
... | ```(1) To fire a new keyvalue struct, three parameters should be     provided in the following manner:         DispatchKeyValue(entity, "KeyName", "Value");     The "szClassName" value will automatically use the classname     of the specified entity, "fHandled" will be set to 0. (2) Inside the pfn_keyvalue() forward this native can be used to     modify the keyvalue struct inline, two parameters should be     provided in the following manner:        DispatchKeyValue("KeyName", "Value");     The "szClassName" or "fHandled" values can not be changed.```
---|---
#### Description
```
Fires/sets a keyvalue on an entity.
```

#### Return
```
This function has no return value.
```

#### Error
```
For variant (1), if an invalid entity index is provided, an
error will be thrown. For variant (2), if it is used outside of
the pfn_keyvalue() forward, an error will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

