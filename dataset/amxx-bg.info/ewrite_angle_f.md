# ewrite_angle_f
#### Syntax
```
native ewrite_angle_f(Float:x);
```

#### Usage
x | ```Angle to write```
---|---
#### Description
```
Writes an angle entry to a message using a float value.
```

#### Note
```
This function should only be used in between a emessage_begin()
or emessage_begin_f() and a emessage_end() function. Trying to use
it outside of these functions will crash the server immediately.
```

#### Return
```
This function has no return value.
```


This code is a part of messages.inc. To use this code you should include messages.inc as ```#include <messages>```


  
  

