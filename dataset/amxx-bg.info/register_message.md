# register_message
#### Syntax
```
native register_message(iMsgId, const szFunction[]);
```

#### Usage
iMsgId | ```Message id```
---|---
szFunction | ```Function that will be called```
#### Description
```
Lets you directly hook a message in the engine.
```

#### Note
```
The function is called in the following manner:
  msg_id          - Message id
  msg_dest        - Destination type (see MSG_* constants in messages_const.inc)
  msg_entity      - Entity receiving the message
```

#### Note
```
You can overwrite the message before anything happens by using the
set_msg_arg_* functions and either let the message continue by
returning PLUGIN_CONTINUE or fully block it with PLUGIN_HANDLED.
```

#### Note
```
If you hook a message, the message is stored but not sent. You have
the opportunity to not only execute code, but to get/set the contents
of the message before you choose to either block it or let it go on
its way.
```

#### Note
```
The return value can be passed to unregister_message() in order to
stop the message from being hooked.
```

#### Return
```
Id that can be passed to unregister_message() on
success, or 0 if an invalid message id is passed
```

#### Error
```
If the specified function can't be found, an
error will be thrown.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

