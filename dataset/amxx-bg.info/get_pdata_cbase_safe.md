# get_pdata_cbase_safe
#### Syntax
```
native get_pdata_cbase_safe(id, offset, linuxdiff=5, macdiff=5);
```

#### Usage
id | ```Entry to examine the private data.```
---|---
offset | ```The windows offset of the data.```
linuxdiff | ```The linux difference of the data.```
macdiff | ```The mac os x difference of the data.```
#### Description
```
This is similar to the get_pdata_cbase, however it does not dereference memory.
This is many times slower than get_pdata_cbase, and this should only be used
for testing and finding of offsets, not actual release quality plugins.
This will return an index of the corresponding cbase field in private data.
Returns -1 on a null entry. -2 on an invalid entry.
```

#### Return
```
The index of the corresponding pdata field, -1 for null, -2 for invalid.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

