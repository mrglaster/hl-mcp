# ArraySortEx
#### Syntax
```
native ArraySortEx(Array:array, const comparefunc[], data[]="", data_size=0);
```

#### Usage
array | ```Array handle```
---|---
comparefunc | ```Callback function used for comparison```
data | ```Extra data that is passed through to the callback```
data_size | ```Size of extra data```
#### Description
```
A faster version of ArraySort, the sorting algorithm then uses the custom
comparison function to sort the data.
```

#### Note
```
The advantage of this function is that the data of the elements being
compared is directly passed to the function, instead of the item
indexes that are passed by ArraySort. This removes the need for calling
ArrayGet[Cell|String|Array] every time before being able to compare the
elements.
```

#### Note
```
For Arrays with a cellsize of 1 (used for storing integers and floats),
the function is called in the following manner:

public MySortFunc(Array:array, elem1, elem2, const data[], data_size)

  array           - Array handle in its current un-sorted state
  elem1, elem2    - Current element pair being compared
  data[]          - Extra data array passed to the sort func
  data_size       - Size of extra data
```

#### Note
```
For Arrays with a cellsize larger than 1 (used for storing arrays and
strings), the function is called in the following manner:

public MySortFunc(Array:array, elem1[], elem2[], const data[], data_size)

  array               - Array handle in its current un-sorted state
  elem1[], elem2[]    - Current element pair being compared
  data[]              - Extra data array passed to the sort func
  data_size           - Size of extra data
```

#### Note
```
The comparison function should return:
  -1 if elem1 should go before elem2
   0 if elem1 and elem2 are equal
   1 if elem1 should go after elem2
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


  
  

