et_time
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_time - Returns time in given format. The most popular is: "%m/%d/%Y - %H:%M:%S". 
Syntax
get_time ( const format[],output[],len ) 
Type
Native 
Notes
Example   
`    
new CurrentTime[9]   
get_time("%H:%M:%S",CurrentTime,8)   
client_print(0,3,"The current time is: %s",CurrentTime)   
  `
