# CreateStack
#### Syntax
```
native Stack:CreateStack(blocksize = 1);
```

#### Usage
blocksize | ```The number of cells each entry in the stack can hold```
---|---
#### Description
```
Creates a stack structure. A stack is a LIFO (last in, first out) vector of
of items. It has O(1) insertion and O(1) removal.
```

#### Note
```
Stacks provide only two operations: Push (adding an item to the top)
and Pop (remove an item from the top, in reverse-push order).
```

#### Note
```
The contents of the stack are uniform; i.e. storing a string and then
retrieving it as an integer is NOT the same as str_to_num()!
```

#### Note
```
The "blocksize" determines how many cells each stack slot has, it can
not be changed after creation.
```

#### Return
```
New stack Handle, which must be freed via DestroyStack()
```

#### Error
```
If an invalid blocksize is provided an error will be
thrown.
```


This code is a part of cellstack.inc. To use this code you should include cellstack.inc as ```#include <cellstack>```


  
  

