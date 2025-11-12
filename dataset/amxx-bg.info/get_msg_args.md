# get_msg_args
#### Syntax
```
native get_msg_args();
```

#### Description
```
Gets number of arguments that were passed to a message.
```

#### Note
```
This function will fail if used outside a hooked message scope, thus
it should never be used unless inside a registered message function.
```

#### Return
```
Number of arguments
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

