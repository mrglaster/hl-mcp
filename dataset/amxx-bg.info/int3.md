# int3
#### Syntax
```
native int3();
```

#### Description
```
Triggers the software interrupt 3, used for breaking into an attached
debugger.
```

#### Note
```
Warning: This is a debugging function that is not intended for general
plugin use. Using this function will either halt the server and break
into the attached debugger, or outright crash the server if no
debugger is attached.
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

