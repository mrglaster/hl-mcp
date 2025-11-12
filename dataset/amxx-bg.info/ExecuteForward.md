# ExecuteForward
#### Syntax
```
native ExecuteForward(forward_handle, &ret = 0, any:...);
```

#### Usage
forward_handle | ```Forward handle```
---|---
ret | ```Optional variable to store return value in```
... | ```Variable number of parameters to pass through```
#### Description
```
Executes a forward.
```

#### Note
```
Passing arrays requires them to be prepared using PrepareArray()
```

#### Return
```
1 on success, 0 if forward can't be executed
```

#### Error
```
If the number of parameters mismatch from the number
of parameters that the forward was declared with,
an error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

