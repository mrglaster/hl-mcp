# callfunc_begin_i
#### Syntax
```
native callfunc_begin_i(func, plugin = -1);
```

#### Usage
func | ```Function id```
---|---
plugin | ```Plugin filename, if empty the calling plugin is targeted The filename has to be the full exact name (e.g. stats.amxx)```
#### Description
```
Initiates a function call to this or another plugin by function id.
```

#### Note
```
This only sets up the function call and covers the pre-requisites.
Push parameters using the callfunc_push_* set of functions. The call
will be executed only upon using callfunc_end()
```

#### Note
```
The function id can be retrieved by get_func_id()
```

#### Return
```
1 on success
                 -1 if plugin was not found
                 -2 if function is not executable
```

#### Error
```
If called while another callfunc has not yet been finished,
or the specified function is invalid, an error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

