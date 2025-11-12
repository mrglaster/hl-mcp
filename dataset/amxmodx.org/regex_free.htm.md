egex_free
[Regex](http://127.0.0.1:8000/content/index.htm) (regex.inc) 
Description
regex_free - Frees regex handle 
Syntax
regex_free ( &Regex:id ) 
Type
Native 
Notes
Frees the memory associated with a regex results and sets the handle to 0.   
You must do this if the handle >=1 or REGEX_OK, once you're done using the information, or you will have memory leaks.   

