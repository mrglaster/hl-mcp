et_task
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
set_task - Calls function on specified time. 
Syntax
set_task ( Float:time,const function[],id = 0,parameter[]="",len = 0,flags[]="", repeat = 0 ) 
Type
Native 
Notes
Flags:   
"a" - repeat.   
"b" - loop task.   
"c" - do task on time after a map timeleft.   
"d" - do task on time before a map timelimit.   
  
Example of executing a task once.   
`    
set_task(15.0,"MyFunction")   
  `   
  
Remember that functions executed by set_task needs be public   

