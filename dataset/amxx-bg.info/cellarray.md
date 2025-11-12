# Functions in cellarray.inc
Function | Description  
---|---  
[ByteCountToCells](https://amxx-bg.info/api/cellarray/ByteCountToCells) | ```
Returns the number of cells required to fit a string of the specified size
(including the null terminator).
```
  
[ArrayCreate](https://amxx-bg.info/api/cellarray/ArrayCreate) | ```
Creates a handle to a dynamically sized array.
```
  
[ArrayClone](https://amxx-bg.info/api/cellarray/ArrayClone) | ```
Clones an array, returning a new handle with the same size and data.
```
  
[ArrayClear](https://amxx-bg.info/api/cellarray/ArrayClear) | ```
Clears all entries from the array.
```
  
[ArraySize](https://amxx-bg.info/api/cellarray/ArraySize) | ```
Returns the number of elements in the array.
```
  
[ArrayResize](https://amxx-bg.info/api/cellarray/ArrayResize) | ```
Resizes an array.
```
  
[ArrayGetArray](https://amxx-bg.info/api/cellarray/ArrayGetArray) | ```
Retrieves an array of data from a cellarray.
```
  
[ArrayGetCell](https://amxx-bg.info/api/cellarray/ArrayGetCell) | ```
Returns a single cell of data from an array
```
  
[ArrayGetString](https://amxx-bg.info/api/cellarray/ArrayGetString) | ```
Returieves string data from an array.
```
  
[ArraySetArray](https://amxx-bg.info/api/cellarray/ArraySetArray) | ```
Fills an item's data with the contents of an array.
```
  
[ArraySetCell](https://amxx-bg.info/api/cellarray/ArraySetCell) | ```
Sets an item's data to a single cell value.
```
  
[ArraySetString](https://amxx-bg.info/api/cellarray/ArraySetString) | ```
Sets an item's data to a string value.
```
  
[ArrayPushArray](https://amxx-bg.info/api/cellarray/ArrayPushArray) | ```
Creates a new item at the end of the cellarray and copies the provided array
into it.
```
  
[ArrayPushCell](https://amxx-bg.info/api/cellarray/ArrayPushCell) | ```
Creates a new item at the end of the array and sets the item's single cell
value.
```
  
[ArrayPushString](https://amxx-bg.info/api/cellarray/ArrayPushString) | ```
Creates a new item at the end of the array and copies the provided string
into it.
```
  
[ArrayInsertArrayAfter](https://amxx-bg.info/api/cellarray/ArrayInsertArrayAfter) | ```
Creates a new item behind the specified item and copies the provided array
into it. All items beyond it get shifted up by one.
```
  
[ArrayInsertCellAfter](https://amxx-bg.info/api/cellarray/ArrayInsertCellAfter) | ```
Creates a new item behind the specified item and sets the item's single cell
value. All items beyond it get shifted up by one.
```
  
[ArrayInsertStringAfter](https://amxx-bg.info/api/cellarray/ArrayInsertStringAfter) | ```
Creates a new item behind the specified item and copies the provided string
into it. All items beyond it get shifted up by one.
```
  
[ArrayInsertArrayBefore](https://amxx-bg.info/api/cellarray/ArrayInsertArrayBefore) | ```
Creates a new item in front of the specified item and copies the provided
array into it. All items beyond it get shifted up by one.
```
  
[ArrayInsertCellBefore](https://amxx-bg.info/api/cellarray/ArrayInsertCellBefore) | ```
Creates a new item in front of the specified item and sets the item's single
cell value. All items beyond it get shifted up by one.
```
  
[ArrayInsertStringBefore](https://amxx-bg.info/api/cellarray/ArrayInsertStringBefore) | ```
Creates a new item in front of the specified item and copies the provided
string into it. All items beyond it get shifted up by one.
```
  
[ArraySwap](https://amxx-bg.info/api/cellarray/ArraySwap) | ```
Swaps the position of two items.
```
  
[ArrayDeleteItem](https://amxx-bg.info/api/cellarray/ArrayDeleteItem) | ```
Deletes an item from the array. All items beyond it get shifted down by one.
```
  
[ArrayFindString](https://amxx-bg.info/api/cellarray/ArrayFindString) | ```
Searches through the array and returns the index of the first occurence of
the specified string.
```
  
[ArrayFindValue](https://amxx-bg.info/api/cellarray/ArrayFindValue) | ```
Searches through the array and returns the index of the first occurence of
the specified value.
```
  
[ArrayGetStringHandle](https://amxx-bg.info/api/cellarray/ArrayGetStringHandle) | ```
Creates a special handle that can be passed to a string format routine for
printing as a string (with the %a format option).
```
  
[ArrayDestroy](https://amxx-bg.info/api/cellarray/ArrayDestroy) | ```
Destroys the array and frees its memory.
```
  
[ArraySort](https://amxx-bg.info/api/cellarray/ArraySort) | ```
Similar to sorting.inc's CustomSort, the sorting algorithm then uses the
custom comparison function to sort the data.
```
  
[ArraySortEx](https://amxx-bg.info/api/cellarray/ArraySortEx) | ```
A faster version of ArraySort, the sorting algorithm then uses the custom
comparison function to sort the data.
```
  

This code is a part of cellarray.inc. To use this code you should include cellarray.inc as ```#include <cellarray>```


  
  

