# okapi_set_param
#### Syntax
```
native okapi_set_param(param_id, any:...);
```

#### Usage
param_id | ```Index of the parameter. First is 1.```
---|---
... | ```Value of the parameter```
#### Description
```
Modifies a parameter that will be passed in the call to the original function.
```

#### Return
```
This function has no return value.
```

#### Error
```
Not inside a hook
Invalid parameter count
Invalid parameter index
```


This code is a part of okapi.inc. To use this code you should include okapi.inc as ```#include <okapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.