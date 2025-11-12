# unregister_message
#### Syntax
```
native unregister_message(iMsgId, registeredmsg);
```

#### Usage
iMsgId | ```Message id```
---|---
registeredmsg | ```Registered message id```
#### Description
```
Unregisters a message hook previously created with register_message().
```

#### Note
```
You must pass the proper message id and return value from the
message to unregister the message successfully.
```

#### Return
```
Id that can again be passed to register_message() on
success, or 0 if an invalid message id is passed
```

#### Error
```
If an invalid registered message handle is passed, an
error will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

