# crxknives_attempt_change
#### Syntax
```
forward crxknives_attempt_change(id, knife)
```

#### Usage
id | ```Client index```
---|---
knife | ```Knife index```
#### Description
```
Called when the client attempts to change his knife model.
```

#### Return
```
PLUGIN_HANDLED to prevent the client from changing his knife,
PLUGIN_CONTINUE to allow the change
```


This code is a part of crxknives.inc. To use this code you should include crxknives.inc as ```#include <crxknives>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.