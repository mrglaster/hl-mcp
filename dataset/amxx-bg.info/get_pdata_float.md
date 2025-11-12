# get_pdata_float
#### Syntax
```
native Float:get_pdata_float(_index, _Offset, _linuxdiff = 5, _macdiff = 5);
```

#### Usage
_index | ```Entity index.```
---|---
_Offset | ```Offset to search.```
_linuxdiff | ```Linux difference.```
_macdiff | ```Mac OS X difference.```
#### Description
```
Returns a float from an entity's private data.

_linuxdiff value is what to add to the _Offset for linux servers.
_macdiff value is what to add to the _Offset for os x servers.

A log error is thrown on invalid _index and _Offset.
```

#### Return
```
An float value is returned.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

