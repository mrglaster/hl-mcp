# callfunc_push_intrf
#### Syntax
```
native callfunc_push_intrf(&value);
```

#### Usage
value | ```Int value to push```
---|---
#### Description
```
Pushes an int value reference onto the current call.
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


  
  

