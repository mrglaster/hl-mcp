# Functions in sorting.inc
Function | Description  
---|---  
[SortIntegers](https://amxx-bg.info/api/sorting/SortIntegers) | ```
Basic sorting functions below.
```
  
[SortFloats](https://amxx-bg.info/api/sorting/SortFloats) | ```
This function has no description.
```
  
[SortStrings](https://amxx-bg.info/api/sorting/SortStrings) | ```
This function has no description.
```
  
[SortCustom1D](https://amxx-bg.info/api/sorting/SortCustom1D) | ```
Sorts a custom 1D array.  You must pass in a comparison function.
The sorting algorithm then uses your comparison function to sort the data.
The function is called in the following manner:

public MySortFunc(elem1, elem2, const array[], const data[], data_size)

 elem1, elem2    - Current element pair being compared
 array[]         - Array in its current mid-sorted state.
 data[]          - Extra data array you passed to the sort func.
 data_size       - Size of extra data you passed to the sort func.

Your function should return:
 -1 if elem1 should go before elem2
  0 if elem1 and elem2 are equal
  1 if elem1 should go after elem2
Note that the parameters after elem2 are all optional and you do not need to specify them.
```
  
[SortCustom2D](https://amxx-bg.info/api/sorting/SortCustom2D) | ```
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
  
[SortADTArray](https://amxx-bg.info/api/sorting/SortADTArray) | ```
Sort an ADT Array. Specify the type as Integer, Float, or String.
```
  

This code is a part of sorting.inc. To use this code you should include sorting.inc as ```#include <sorting>```


  
  

