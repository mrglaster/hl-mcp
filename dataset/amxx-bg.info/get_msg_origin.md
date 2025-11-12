# get_msg_origin
#### Syntax
```
native get_msg_origin(const Float:_Origin[3]);
```

#### Usage
_Origin | ```Array to store the origin in```
---|---
#### Description
```
Gets the origin of a message.
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
If the function is used outside a message hook, an
error will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

