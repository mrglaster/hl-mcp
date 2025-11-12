# set_pdata_short
#### Syntax
```
native set_pdata_short(_index, _offset, _value, _linuxdiff = 20, _macdiff = 20);
```

#### Usage
_index | ```Entity index.```
---|---
_offset | ```Offset to search.```
_value | ```Value to set.```
_linuxdiff | ```Linux difference.```
_macdiff | ```Mac OS X difference.```
#### Description
```
Sets a short value to an entity's private data.

This function is byte-addressable.  Unlike set_pdata_int() which searches in byte increments of 4,
set_pdata_short searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```

#### Return
```
1 on success.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

