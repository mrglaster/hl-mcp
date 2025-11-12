# zp_set_user_model
#### Syntax
```
native zp_set_user_model(id, const model[])
```

#### Usage
id | ```Player index who's model needs to be set.```
---|---
model | ```String containing the model folder name.```
#### Description
```
Properly sets the given model for the player.

Note: You should use this native for setting a player's model
instead of other methods.

Note: The model name which is passed should be the model's folder
name for eg: zombie_source and the folder should contain the
actual model file in it eg: zombie_source.mdl

Note: The model you are setting should be precached in the
sub-plugin using the plugin_precache forward to prevent problems.

Note: It is highly advised to set the models with an additional
delay during round start to prevent SVC_BAD errors/kicks.
```


This code is a part of zombie_plague_advance.inc. To use this code you should include zombie_plague_advance.inc as ```#include <zombie_plague_advance>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.