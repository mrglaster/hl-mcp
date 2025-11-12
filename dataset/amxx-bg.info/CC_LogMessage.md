# CC_LogMessage
#### Syntax
```
stock CC_LogMessage(id, const file[] = "", const input[], any:...)
```

#### Usage
id | ```Client index (use 0 to send to all players)```
---|---
file | ```The log file that will be used```
input | ```The message to send```
... | ```Variable number of formatting parameters```
#### Description
```
Sends a colored chat message and logs it at the same time.
```

#### Note
```
If the file name is not set, the default log file will be used instead.
```

#### Return
```
Length of the printed message
```


This code is a part of cromchat.inc. To use this code you should include cromchat.inc as ```#include <cromchat>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.