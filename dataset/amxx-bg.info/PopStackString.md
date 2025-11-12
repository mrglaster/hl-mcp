# PopStackString
#### Syntax
```
native bool:PopStackString(Stack:handle, buffer[], maxlength, &written = 0);
```

#### Usage
handle | ```Stack handle```
---|---
buffer | ```Buffer to copy string to```
maxlength | ```Maximum size of the buffer```
written | ```Variable to store number of characters copied to```
#### Description
```
Pops a string value from a stack.
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


  
  

