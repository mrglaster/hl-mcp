# set_pdata_cbase
#### Syntax
```
native set_pdata_cbase(id, offset, value, linuxdiff=5, macdiff=5);
```

#### Usage
id | ```The entity to examine the private data.```
---|---
offset | ```The windows offset of the data.```
value | ```The index to store, -1 for invalid```
linuxdiff | ```The linux difference of the data.```
macdiff | ```The mac os x difference of the data.```
#### Description
```
This is used to compliment fakemeta's {get,set}_pdata_{int,float,string}.
This requires the mod to have the pev and base fields set in hamdata.ini.
This will set the corresponding cbase field in private data with the index.
Pass -1 to null the entry.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

