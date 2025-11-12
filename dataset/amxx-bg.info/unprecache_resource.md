# unprecache_resource
#### Syntax
```
native bool:unprecache_resource(szResource[], iType, bool:bForceChange, szNewResource[] = "")
```

#### Usage
szResource[] | ```Buffer to store resource name.```
---|---
iType | ```Type of the resource. See _:ResourceData Enum```
bForceChange | ```If true, the map will be restarted to apply changes instantly```
szNewResource[] | ```New resource name, if the iType is REPLACE```
#### Description
```
Adds a file for removal or replace.
```

#### Type
```
Boolean
```

#### Return
```
True if it could be added to file, false otherwise.
```


This code is a part of precache_list.inc. To use this code you should include precache_list.inc as ```#include <precache_list>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. 