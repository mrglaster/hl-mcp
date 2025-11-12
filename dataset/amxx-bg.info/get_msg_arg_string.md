# get_msg_arg_string
#### Syntax
```
native get_msg_arg_string(argn, szReturn[], iLength);
```

#### Usage
argn | ```Argument number```
---|---
szReturn | ```Buffer to store the value in```
iLength | ```Maximum buffer length```
#### Description
```
Gets the string value from a specified argument.
```

#### Note
```
This function will fail if used outside a hooked message scope, thus
it should never be used unless inside a registered message function.
```

#### Return
```
String length
```

#### Error
```
If an invalid message argument is passed, an
error will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

