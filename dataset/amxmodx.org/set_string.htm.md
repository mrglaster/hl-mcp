et_string
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
set_string - Sets a string in a calling plugin 
Syntax
set_string ( param, string[], maxlen ) 
Type
Native 
Notes
This can only be used in a dynamic native function registered with style 0 (default). Arguments start at 1.   
  
Copies a string back into a buffer specified in a parameter. For example:   
` public mynative(id, numParams)   
  
   set_string(1, "Yams", 4)   
}   
public test()   
  
   new str[5]   
   mynative(str)   
}   
  `   
Will copy the word "Yams" into the array given as parameter 1.
