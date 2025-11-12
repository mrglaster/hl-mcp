# CC_GroupMessage
#### Syntax
```
stock CC_GroupMessage(const flags[] = "", const params[] = "", const input[], any:...)
```

#### Usage
flags | ```Filtering flags```
---|---
params | ```String to match against if the flags require it```
input | ```The message to send```
... | ```Variable number of formatting parameters```
#### Description
```
Sends a colored chat message to a group of players matching the flags from the get_players() function.
```

#### Note
```
The filtering flags are the same that are used by the get_players() function
```

#### Return
```
Length of the printed message or 0 if no players were matched
```


This code is a part of cromchat.inc. To use this code you should include cromchat.inc as ```#include <cromchat>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.