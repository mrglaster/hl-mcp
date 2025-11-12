# PopStackArray
#### Syntax
```
native bool:PopStackArray(Stack:handle, any:buffer[], size = -1);
```

#### Usage
handle | ```Stack handle```
---|---
buffer | ```Array to copy value to```
size | ```Size of buffer, if not set (-1) assumes the size is equal to the stack blocksize```
#### Description
```
Pops an array of cells from a stack.
```

#### Return
```
True on success, false if the stack is empty
```

#### Error
```
If an invalid handle is provided an error will be thrown.
```


This code is a part of cellstack.inc. To use this code you should include cellstack.inc as ```#include <cellstack>```


  
  

