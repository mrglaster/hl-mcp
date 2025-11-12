# DestroyStack
#### Syntax
```
native DestroyStack(&Stack:handle);
```

#### Usage
handle | ```Stack to destroy```
---|---
#### Description
```
Destroys a stack and frees its memory.
```

#### Note
```
The function automatically sets the variable passed to it to 0 to aid
in preventing accidental usage after destroy.
```

#### Return
```
1 if the Stack was destroyed, 0 if nothing had to be
destroyed (invalid handle)
```


This code is a part of cellstack.inc. To use this code you should include cellstack.inc as ```#include <cellstack>```


  
  

