# cm_set_user_say_format
#### Syntax
```
native cm_set_user_say_format(id, say[], say_team[])
```

#### Usage
id | ```Player's index.```
---|---
say | ```Temporary say format.```
say_team | ```Temporary say_team format.```
#### Description
```
Sets a temporary say format on the client.
```

#### Note
```
The say format set with this native won't get saved in the .ini file, so it will be gone after the client's data is updated.
```

#### Return
```
0 if the format doesn't exist, 1 otherwise.
```


This code is a part of chatmanager.inc. To use this code you should include chatmanager.inc as ```#include <chatmanager>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.