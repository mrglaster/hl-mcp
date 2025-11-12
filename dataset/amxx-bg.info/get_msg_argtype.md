# get_msg_argtype
#### Syntax
```
native get_msg_argtype(argn);
```

#### Usage
argn | ```Argument number```
---|---
#### Description
```
Gets the argument type of a specified argument.
```

#### Note
```
This function will fail if used outside a hooked message scope, thus
it should never be used unless inside a registered message function.
```

#### Return
```
Argument type (see ARG_* constants in message_const.inc)
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

