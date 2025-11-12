# PushStackCell
#### Syntax
```
native PushStackCell(Stack:handle, any:value);
```

#### Usage
handle | ```Stack handle```
---|---
value | ```Value to push```
#### Description
```
Pushes a value onto the end of the stack, adding a new index.
```

#### Note
```
This may safely be used even if the stack has a blocksize greater than
1.
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


  
  

