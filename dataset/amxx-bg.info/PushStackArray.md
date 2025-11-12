# PushStackArray
#### Syntax
```
native PushStackArray(Stack:handle, const any:values[], size= -1);
```

#### Usage
handle | ```Stack handle```
---|---
values | ```Block of values to copy```
size | ```If not set, the number of elements copied from the array will be equal to the blocksize, if set higher than the blocksize, the operation will be truncated,```
#### Description
```
Pushes an array of cells onto the end of a stack. The cells are pushed as a
block (i.e. the entire array takes up one stack slot), rather than pushing
each cell individually.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid handle is provided or the resizing
operation runs out of memory, an error will be thrown.
```


This code is a part of cellstack.inc. To use this code you should include cellstack.inc as ```#include <cellstack>```


  
  

