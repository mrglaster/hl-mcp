# nnc_user_name_changed
#### Syntax
```
forward nnc_user_name_changed(id, oldname[], newname[])
```

#### Usage
id | ```Client index```
---|---
oldname | ```Old name```
newname | ```New name```
#### Description
```
Called when a player attemtps to change his name
```

#### Return
```
NNC_CONTINUE not to change the behavior
NNC_BLOCK to block the name change
NNC_ALLOW to allow the name change, ignoring all other checks
```


This code is a part of nnc.inc. To use this code you should include nnc.inc as ```#include <nnc>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.