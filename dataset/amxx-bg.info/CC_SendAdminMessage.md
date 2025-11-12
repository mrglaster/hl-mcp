# CC_SendAdminMessage
#### Syntax
```
stock CC_SendAdminMessage(const flags[] = "", bool:allflags = true, const input[], any:...)
```

#### Usage
flags | ```Admin flags```
---|---
allflags | ```If set to true it will match players who have ALL of the specified admin flags, otherwise it will match players with ANY of the flags```
input | ```The message to send```
... | ```Variable number of formatting parameters```
#### Description
```
Sends a colored chat message to all players who have the specified admin flags.
```

#### Return
```
Length of the printed message or 0 if no players were matched
```


This code is a part of cromchat.inc. To use this code you should include cromchat.inc as ```#include <cromchat>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.