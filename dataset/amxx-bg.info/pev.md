# pev
#### Syntax
```
native pev(_index,_value,any:...);
```

#### Usage
_index | ```The entity index to lookup.```
---|---
_value | ```The pev field to lookup (look in fakemeta_const.inc)```
#### Description
```
Returns entvar data from an entity.  Use the pev_* enum (in fakemeta_const.inc) to specify which data you want retrieved.
```

#### Note
```
This function uses "read_data" style data syntax.  It returns integer values,
    by-references float data, and sets a buffer for string data.
```

#### Note
```
If retrieving strings, you may optionally get a pointer into the global string table. Depending on
your situation, there are two ways to do this.
1: This simply gets the pointer.
   new ptr = pev(entid, pev_classname)
2: The pointer will be stored in ptr AND the actual string is retrieved.
   new ptr, classname[32]
   pev(entid, pev_classname, ptr, classname, 31)
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

