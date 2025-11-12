# get_grenade_id
#### Syntax
```
native get_grenade_id(id, model[], len, grenadeid = 0);
```

#### Usage
id | ```Owner entity index to match```
---|---
model | ```Buffer to copy grenade model to```
len | ```Maximum length of buffer```
grenadeid | ```Entity index to start searching from```
#### Description
```
Finds a grenade entity, matching by owner.
```

#### Return
```
Grenade entity index > 0 if found, 0 otherwise
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

