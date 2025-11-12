egister_dictionary
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
register_dictionary - Registers a dictionary file 
Syntax
register_dictionary ( const file[] ) 
Type
Native 
Notes
The file must be located relative to "%datadir%/lang". The file should be formatted like a language dictionary file. An example would be:   
  
`   
[en]   
hello = Hello!   
bye = Goodbye!   
greeting = Hello, %s!   
   
[es]   
hello = Hola!   
...   
`   
  
The dictionary implementation in AMX Mod X is called "register" because it only adds or enforces the dictionary when necessary. The text file is not processed if it has already been processed and has not changed.
