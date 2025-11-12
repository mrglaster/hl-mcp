# RegisterMessage
#### Syntax
```
native MessageHook:RegisterMessage(const msg_id, const callback[], post = 0);
```

#### Usage
msg_id | ```The ID of the message to register the callback for.```
---|---
callback | ```The name of the callback function.```
post | ```Whether the callback should be invoked before or after processing the message. (optional)```
#### Description
```
Registers a callback function to be called when a game message with the specified ID is received.
```

#### Note
```
The callback arguments have:
  msg_id          - Message id
  msg_dest        - Destination type (see MSG_* constants in messages_const.inc)
  msg_entity      - Entity receiving the message
```

#### Note
```
You can modify the message content using SetMessageData native before the original function is invoked.
Also can reading the message content using GetMessageData native.

In the callback function, use the return values from Hookchain return types, such as HC_CONTINUE, HC_SUPERCEDE, etc.
to control the flow of message processing.
```

#### Return
```
Returns a handle to the registered message hook.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.