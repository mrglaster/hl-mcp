# crxknives_get_attribute_int
#### Syntax
```
native bool:crxknives_get_attribute_int(id, const attribute[], &dest, bool:playerid = true)
```

#### Usage
id | ```Client index```
---|---
attribute | ```Knife attribute```
dest | ```Integer variable to store the value in```
playerid | ```If set to false, the "id" parameter will be treated as a knife index instead```
#### Description
```
Returns the integer value from a knife attribute.
```

#### Return
```
True if the client or knife has that attribute set, false otherwise
```


This code is a part of crxknives.inc. To use this code you should include crxknives.inc as ```#include <crxknives>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.