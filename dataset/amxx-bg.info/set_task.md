# set_task
#### Syntax
```
native set_task(Float:time, const function[], id = 0, const any:parameter[] = "", len = 0, const flags[] = "", repeat = 0);
```

#### Usage
time | ```Time interval to assign```
---|---
function | ```Function to execute```
id | ```Task id to assign```
parameter | ```Data to pass through to callback```
len | ```Size of data```
flags | ```Optional set of flags:   "a" - repeat timer a set amount of times   "b" - loop indefinitely until timer is stopped   "c" - time interval is treated as absolute time after         map start   "d" - time interval is treated as absolute time before         map change```
repeat | ```If the "a" flag is set, the task will be repeated this many times```
#### Description
```
Calls a function after a specified time has elapsed.
```

#### Note
```
Please consider using set_task_ex() instead which allows you to
use named constants for flags instead of letters.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid callback function is provided, an error is
thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

