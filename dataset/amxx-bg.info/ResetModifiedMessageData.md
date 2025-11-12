# ResetModifiedMessageData
#### Syntax
```
native bool:ResetModifiedMessageData(MsgDataType:type = MsgAny, const number = -1);
```

#### Usage
type | ```The type of the data to check for modification This can be one of the following: - MsgAny:      Reset all modified message data to its original values - MsgDest:     Reset the destination to its original value - MsgIndex:    Reset the message ID to its original value - MsgOrigin:   Reset the origin to its original value - MsgTargetId: Reset the index of the recipient client to its original value - MsgArg:      Reset a specific argument of the message to its original value```
---|---
number | ```The number of the argument to reset (used only when type is MsgDataType:MsgArg) Default value is -1, which means all arguments will be reset.```
#### Description
```
Resets a specific type of message data to its original value
```

#### Return
```
Returns true if the modified data type was reset, otherwise false.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.