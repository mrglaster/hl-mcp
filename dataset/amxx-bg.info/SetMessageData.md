# SetMessageData
#### Syntax
```
native bool:SetMessageData(const MsgDataType:type, any:...);
```

#### Usage
type | ```The type of the message data that can be changed```
---|---
... | ```Additional args depending on the type of the message argument being retrieved (For more details, look at the enum MsgArgType)```
#### Description
```
Sets the message data in the current game message.
```

#### Return
```
Returns true if the message data is successfully set, otherwise false.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.