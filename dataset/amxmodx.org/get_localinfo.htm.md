et_localinfo
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_localinfo - Gets an info value ( 
Syntax
get_localinfo ( const info[], output[], len ) 
Type
Native 
Notes
Result is stored in the output array for a maximum length of len characters.   
  
example:   
`    
get_localinfo("amxx_basedir",name,len)   
  `   
  
Type "localinfo" in the hlds console to see a list the information can can be retrived
