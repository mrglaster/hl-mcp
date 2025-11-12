# SortCustom2D
#### Syntax
```
native SortCustom2D(array[][], array_size, const comparefunc[], data[]="", data_size=0);
```

#### Description
```
Sorts a custom 2D array.
The sorting algorithm then uses your comparison function to sort the data.
The function is called in the following manner:

public MySortFunc(const elem1[], const elem2[], const array[], data[], data_size)

 elem1[], elem2[] - Current element array pairs being compared
 array[][]        - Array in its currently being sorted state.
 data[]           - Extra data array you passed to the sort func.
 data_size        - Size of extra data you passed to the sort func.

Your function should return:
 -1 if elem1[] should go before elem2[]
  0 if elem1[] and elem2 are equal[]
  1 if elem1[] should go after elem2[]
Note that the parameters after elem2[] are all optional and you do not need to specify them.
```


This code is a part of sorting.inc. To use this code you should include sorting.inc as ```#include <sorting>```


  
  

