# set_msg_arg_string
#### Syntax
```
native set_msg_arg_string(argn, const szString[]);
```

#### Usage
argn | ```Argument number```
---|---
szString | ```Argument value```
#### Description
```
Sets the string value of a specified argument.
```

#### Note
```
This function will fail if used outside a hooked message scope, thus
it should never be used unless inside a registered message function.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid message argument is passed, an
error will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

