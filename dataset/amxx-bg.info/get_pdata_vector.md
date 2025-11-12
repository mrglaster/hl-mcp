# get_pdata_vector
#### Syntax
```
native get_pdata_vector(_index, _offset, Float:_output[3], _linuxdiff = 20, _macdiff = 20);
```

#### Usage
_index | ```Entity index.```
---|---
_offset | ```Offset to search.```
_output | ```Vector returned by reference.```
_linuxdiff | ```Linux difference.```
_macdiff | ```Mac OS X difference.```
#### Description
```
Returns a vector from an entity's private data.

This function is byte-addressable. Unlike get_pdata_int() which searches in byte increments of 4,
get_pdata_vector searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```

#### Return
```
1 on success.
```


This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

