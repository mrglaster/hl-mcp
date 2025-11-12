# CC_ShowActivityId
#### Syntax
```
stock CC_ShowActivityId(target, id, const name[], const input[], any:...)
```

#### Usage
target | ```Client index to display message to```
---|---
id | ```Client index performing the action```
name | ```Name of client performing the action```
input | ```Formatting rules```
... | ```Variable number of formatting parameters```
#### Description
```
Sends a colored chat message to a single client that obeys the amx_show_activity cvar.
```

#### Note
```
This function is made to mimic the show_activity_id() function, but sends a
colored chat message instead using the CC_SendMessage() function. This means
that the default AMXX function can directly be replaced with this one in order
for it to display a colored chat message rather than a default one.
```

#### Note
```
By default, cromchat.inc will replace all show_activity_id() functions in the file
with the CC_ShowActivityId() function. You can disable this feature by adding
#define CC_DONT_OVERWRITE_ACTIVITY before #include <cromchat> in your plugin.
```

#### Return
```
This function has no return value.
```


This code is a part of cromchat.inc. To use this code you should include cromchat.inc as ```#include <cromchat>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.