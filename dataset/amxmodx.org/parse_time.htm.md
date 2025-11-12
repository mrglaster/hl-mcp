arse_time
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
parse_time - Returns time in input and additionaly fills missing information 
Syntax
parse_time ( const input[],const format[], time = -1 ) 
Type
Native 
Notes
Example:   
`    
parset_time( "10:32:54 04/02/2003", "%H:%M:%S %m:%d:%Y" )   
  `   
For more information see strptime(...) function from C libraries. */
