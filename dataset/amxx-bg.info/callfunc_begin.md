# callfunc_begin
#### Syntax
```
native callfunc_begin(const func[], const plugin[] = "");
```

#### Usage
func | ```Function name```
---|---
plugin | ```Plugin filename, if empty the calling plugin is targeted The filename has to be the full exact name (e.g. stats.amxx)```
#### Description
```
Initiates a function call to this or another plugin by function name.
```

#### Note
```
This only sets up the function call and covers the pre-requisites.
Push parameters using the callfunc_push_* set of functions. The call
will be executed only upon using callfunc_end()
```

#### Return
```
1 on success
0 on runtime error
                 -1 if plugin was not found
                 -2 if function was not found
```

#### Error
```
If called while another callfunc has not yet been finished,
an error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

