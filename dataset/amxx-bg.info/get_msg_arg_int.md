# get_msg_arg_int
#### Syntax
```
native get_msg_arg_int(argn);
```

#### Usage
argn | ```Argument number```
---|---
#### Description
```
Gets the integer value of a specified argument.
```

#### Note
```
This function will fail if used outside a hooked message scope, thus
it should never be used unless inside a registered message function.
```

#### Return
```
Argument value as an integer
```

#### Error
```
If an invalid message argument is passed, an
error will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

