# callfunc_push_floatrf
#### Syntax
```
native callfunc_push_floatrf(&Float:value);
```

#### Usage
value | ```Float value to push```
---|---
#### Description
```
Pushes a float value reference onto the current call.
```

#### Note
```
Changes made to this value by the called function will be reflected
in the calling plugin.
```

#### Return
```
This function has no return value.
```

#### Error
```
If called without initiating a callfunc, or the maximum
amount of parameters is reached, an error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

