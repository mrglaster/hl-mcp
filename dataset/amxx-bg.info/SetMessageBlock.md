# SetMessageBlock
#### Syntax
```
native bool:SetMessageBlock(const msgid, MsgBlockType:type);
```

#### Usage
msgid | ```The ID of the message to set the block type for.```
---|---
type | ```The type of block to set for the message, look at the enum MsgBlockType```
#### Description
```
Sets the block type for the specified message ID.
```

#### Return
```
Returns true if the block type is successfully set, otherwise false.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.