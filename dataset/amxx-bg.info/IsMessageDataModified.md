# IsMessageDataModified
#### Syntax
```
native bool:IsMessageDataModified(MsgDataType:type = MsgAny, const number = -1);
```

#### Usage
type | ```The type of the data to check for modification This can be one of the following: - MsgAny:      Check if any part of the message has been modified - MsgDest:     Check if the destination has been modified - MsgIndex:    Check if the message ID has been modified - MsgOrigin:   Check if the origin has been modified - MsgTargetId: Check if the index of the recipient client has been modified - MsgArg:      Check if a specific argument of the message has been modified```
---|---
number | ```The number of the argument to check for modification (used only when type is MsgDataType:MsgArg) Default value is -1, which means the argument number is not applicable```
#### Description
```
Checks if the specified type of message data has been modified

This native allows you to check if any part of the message data, such as its
destination, type, origin, receiver, or any the specific argument of the message, has been modified
```

#### Return
```
Returns true if the specified data type has been modified, false otherwise
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.