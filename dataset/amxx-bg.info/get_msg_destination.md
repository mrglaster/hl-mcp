# get_msg_destination
#### Syntax
```
stock get_msg_destination(id, bool:reliable)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Used with message stocks. Returns whether or not to use the reliable or
unreliable channel when sending a message according to the params used.
```

#### Return
```
MSG_ONE if "id" is non-zero and "reliable" is true,
MSG_ONE_UNRELIABLE if "id" is non-zero and "reliable" is false,
MSG_ALL if "id" is zero and "reliable" is true,
MSG_BROADCAST if "id" is zero and "reliable" is false.
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.