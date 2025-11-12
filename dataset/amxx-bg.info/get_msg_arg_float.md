# get_msg_arg_float
#### Syntax
```
native Float:get_msg_arg_float(argn);
```

#### Usage
argn | ```Argument number```
---|---
#### Description
```
Gets the float value of a specified argument.
```

#### Note
```
This function will fail if used outside a hooked message scope, thus
it should never be used unless inside a registered message function.
```

#### Return
```
Argument value as a float
```

#### Error
```
If an invalid message argument is passed, an
error will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

