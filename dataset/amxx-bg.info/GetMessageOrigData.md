# GetMessageOrigData
#### Syntax
```
native any:GetMessageOrigData(const MsgDataType:type, any:...);
```

#### Usage
type | ```The type of message data that can be get```
---|---
... | ```Additional args depending on the type of the message argument being retrieved (For more details, look at the enum MsgArgType)```
#### Description
```
Gets the message data original value in the current game message.
```

#### Return
```
Returns original value of argument in the current message
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.