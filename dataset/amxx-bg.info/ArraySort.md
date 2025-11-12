# ArraySort
#### Syntax
```
native ArraySort(Array:array, const comparefunc[], data[]="", data_size=0);
```

#### Usage
array | ```Array handle```
---|---
comparefunc | ```Callback function used for comparison```
data | ```Extra data that is passed through to the callback```
data_size | ```Size of extra data```
#### Description
```
Similar to sorting.inc's CustomSort, the sorting algorithm then uses the
custom comparison function to sort the data.
```

#### Note
```
The function is called in the following manner:

public MySortFunc(Array:array, item1, item2, const data[], data_size)

  array           - Array handle in its current un-sorted state
  item1, item2    - Current item pair being compared
  data[]          - Extra data array passed to the sort func
  data_size       - Size of extra data
```

#### Note
```
The comparison function should return:
  -1 if item1 should go before item2
   0 if item1 and item2 are equal
   1 if item1 should go after item2
```

#### Note
```
All parameters after item2 are optional and do not need to be specified
and used.
```

#### Note
```
Unlike the sorting.inc version, the array passed to the callback is not
in mid-sorted state.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid handle or an invalid callback is provided
an error will be thrown.
```


This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

