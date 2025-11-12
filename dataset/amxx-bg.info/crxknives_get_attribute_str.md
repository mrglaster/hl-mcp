# crxknives_get_attribute_str
#### Syntax
```
native bool:crxknives_get_attribute_str(id, const attribute[], dest[], len, bool:playerid = true)
```

#### Usage
id | ```Client index```
---|---
attribute | ```Knife attribute```
dest | ```Buffer to store the value in```
len | ```Max buffer length```
playerid | ```If set to false, the "id" parameter will be treated as a knife index instead```
#### Description
```
Returns the string value from a knife attribute.
```

#### Note
```
You can also return the knife name by using the "NAME" attribute.
```

#### Return
```
True if the client or knife has that attribute set, false otherwise
```


This code is a part of crxknives.inc. To use this code you should include crxknives.inc as ```#include <crxknives>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.