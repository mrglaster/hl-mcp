# set_task_ex
#### Syntax
```
stock set_task_ex(Float:time, const function[], id = 0, const any:parameter[] = "", len = 0, SetTaskFlags:flags = SetTask_Once, repeat = 0)
```

#### Usage
time | ```Time interval to assign```
---|---
function | ```Function to execute```
id | ```Task id to assign```
parameter | ```Data to pass through to callback```
len | ```Size of data```
flags | ```Optional flags (enum SetTaskFlags); valid flags are:   SetTask_Once - Execute callback once (Default)   SetTask_RepeatTimes - repeat timer a set amount of times   SetTask_Repeat - loop indefinitely until timer is stopped   SetTask_AfterMapStart - time interval is treated as absolute       time after map start   SetTask_BeforeMapChange - time interval is treated as absolute       time before map change```
repeat | ```If the SetTask_RepeatTimes flag is set, the task will be repeated this many times```
#### Description
```
Calls a function after a specified time has elapsed.
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


This code is a part of amxmisc.inc . To use this code you should include amxmisc.inc as ```#include <amxmisc>```


  
  

