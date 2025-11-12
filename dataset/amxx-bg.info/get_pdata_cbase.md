# get_pdata_cbase
#### Syntax
```
native get_pdata_cbase(id, offset, linuxdiff=5, macdiff=5);
```

#### Usage
id | ```The entity to examine the private data.```
---|---
offset | ```The windows offset of the data.```
linuxdiff | ```The linux difference of the data.```
macdiff | ```The mac os x difference of the data.```
#### Description
```
This is used to compliment fakemeta's {get,set}_pdata_{int,float,string}.
This requires the mod to have the pev and base fields set in hamdata.ini.
Note this dereferences memory! Improper use of this will crash the server.
This will return an index of the corresponding cbase field in private data.
Returns -1 on a null entry.
```

#### Return
```
The index of the corresponding pdata field. -1 for none set.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

