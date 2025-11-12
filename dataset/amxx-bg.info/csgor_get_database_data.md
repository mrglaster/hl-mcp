# csgor_get_database_data
#### Syntax
```
native csgor_get_database_data(szHostname[], iHostLen, szUsername[], iUserLen, szPassword[], iPassLen, szDatabase[], iDbLen)
```

#### Usage
szHostname | ```String to retrieve Sql Hostname information.```
---|---
iHostLen | ```Buffer lenght for szHostname parameter.```
szUsername | ```String to retrieve Sql Username information.```
iUserLen | ```Buffer lenght for szUsername parameter.```
szPassword | ```String to retrieve Sql Password information.```
iPassLen | ```Buffer lenght for szPassword parameter.```
szDatabase | ```String to retrieve Sql Database information.```
iDbLen | ```Buffer lenght for szDatabase parameter.```
#### Description
```
Stores database connection information into strings.
```

#### Return
```
-1 if invalid parameters num is passed, 1 on success.
```


This code is a part of csgo_remake.inc. To use this code you should include csgo_remake.inc as ```#include <csgo_remake>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.