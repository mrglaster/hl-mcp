# CC_SendMatched
#### Syntax
```
stock CC_SendMatched(id, player, const input[], any:...)
```

#### Usage
id | ```Client index (use 0 to send to all players)```
---|---
player | ```Matching player's index```
input | ```The message to send```
... | ```Variable number of formatting parameters```
#### Description
```
Sends a colored chat message matching a specific player's color.
```

#### Note
```
You can use the "player" argument to set a specific color instead of matching
it automtaically. To do this, you can use one of the following color arguments:
CC_COLOR_TEAM, CC_COLOR_GREY (or CC_COLOR_WHITE), CC_COLOR_BLUE, CC_COLOR_RED.
```

#### Return
```
Length of the printed message
```


This code is a part of cromchat.inc. To use this code you should include cromchat.inc as ```#include <cromchat>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.