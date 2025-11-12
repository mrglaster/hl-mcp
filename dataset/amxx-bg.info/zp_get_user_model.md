# zp_get_user_model
#### Syntax
```
native zp_get_user_model(id, const model[], maxlen)
```

#### Usage
id | ```Player index who's model is to be retrieved.```
---|---
model | ```String in which the model name will be copied.```
maxlen | ```Number of characters (of the string) to copy.```
#### Description
```
Allows you to properly retrieve a player's model

Note: You should use this native for retrieving a player's
current model instead of other methods

Note: The model name which is retrieved is the model's folder
name for eg: zombie_source and is not the model's actual name.
```


This code is a part of zombie_plague_advance.inc. To use this code you should include zombie_plague_advance.inc as ```#include <zombie_plague_advance>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.