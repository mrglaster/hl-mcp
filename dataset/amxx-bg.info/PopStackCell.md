# PopStackCell
#### Syntax
```
native bool:PopStackCell(Stack:handle, &any:value, block = 0, bool:asChar = false);
```

#### Usage
handle | ```Stack handle```
---|---
value | ```Variable to store the value in```
block | ```Optionally specify which block to read from (useful if the blocksize is > 0)```
asChar | ```Optionally read as a byte instead of a cell```
#### Description
```
Pops a cell value from a stack.
```

#### Return
```
True on success, false if the stack is empty.
```

#### Error
```
If an invalid handle, invalid block or invalid byte is
provided, an error will be thrown.
```


This code is a part of cellstack.inc. To use this code you should include cellstack.inc as ```#include <cellstack>```


  
  

