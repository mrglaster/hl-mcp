ead_flags
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
read_flags - Converts a string into a sum of bits. 
Syntax
read_flags ( const flags[] ) 
Type
Native 
Notes
"a" is 1   
"b" is 2   
"c" is 4   
...   
This function will sum the letters into a bit total. 
User Contributed Notes
downtown1 at gmail dot com | Jul-05-04 22:22:28  
---|---  
Use this to check flags quickly.. "a" is (1<<0) (in binary 0001) "b" is (1<<1) (in binary 0010) "c" is (1<<2) (in binary 0100) etc. With this you could make a loop, i.e. flags = read_flags(szString) for (new i = 0; i < 26; i++) { if ( flags&(1<<i) ) //the flag is set, do something or not } But then again it's quicker only in the machine code sense, because usually you'd want different things depending on different flags.  
  

