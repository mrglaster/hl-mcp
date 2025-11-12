# set_msg_block
#### Syntax
```
native set_msg_block(iMessage, iMessageFlags);
```

#### Usage
iMessage | ```Message id```
---|---
iMessageFlags | ```BLOCK_* constant```
#### Description
```
Sets whether or not an engine message will be blocked.
```

#### Note
```
For a list of message flags, have a look at the BLOCK_* constants
in message_const.inc.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid message id is specified, an error
will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

