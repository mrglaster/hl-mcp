# PushStackString
#### Syntax
```
native PushStackString(Stack:handle, const value[]);
```

#### Usage
handle | ```Stack handle```
---|---
value | ```String to push```
#### Description
```
Pushes a string onto the end of a stack, truncating it if it is too long.
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


  
  

