# Functions in cellstack.inc
Function | Description  
---|---  
[CreateStack](https://amxx-bg.info/api/cellstack/CreateStack) | ```
Creates a stack structure. A stack is a LIFO (last in, first out) vector of
of items. It has O(1) insertion and O(1) removal.
```
  
[PushStackCell](https://amxx-bg.info/api/cellstack/PushStackCell) | ```
Pushes a value onto the end of the stack, adding a new index.
```
  
[PushStackString](https://amxx-bg.info/api/cellstack/PushStackString) | ```
Pushes a string onto the end of a stack, truncating it if it is too long.
```
  
[PushStackArray](https://amxx-bg.info/api/cellstack/PushStackArray) | ```
Pushes an array of cells onto the end of a stack. The cells are pushed as a
block (i.e. the entire array takes up one stack slot), rather than pushing
each cell individually.
```
  
[PopStackCell](https://amxx-bg.info/api/cellstack/PopStackCell) | ```
Pops a cell value from a stack.
```
  
[PopStackString](https://amxx-bg.info/api/cellstack/PopStackString) | ```
Pops a string value from a stack.
```
  
[PopStackArray](https://amxx-bg.info/api/cellstack/PopStackArray) | ```
Pops an array of cells from a stack.
```
  
[IsStackEmpty](https://amxx-bg.info/api/cellstack/IsStackEmpty) | ```
Returns if a stack is empty.
```
  
[PopStack](https://amxx-bg.info/api/cellstack/PopStack) | ```
Pops a value off a stack, ignoring it completely.
```
  
[DestroyStack](https://amxx-bg.info/api/cellstack/DestroyStack) | ```
Destroys a stack and frees its memory.
```
  

This code is a part of cellstack.inc. To use this code you should include cellstack.inc as ```#include <cellstack>```


  
  

