ead_file
[Core](http://127.0.0.1:8000/content/index.htm) (file.inc) 
Description
read_file - Reads a line from a file. 
Syntax
read_file ( const file[], line, text[], len, &txtLen ) 
Type
Native 
Notes
Returns index of next line or 0 when the end of the file is reached.   
  
Line numbers start at 0. The line is read into text for a maximum of len characters. The number of characters read is stored in txtLen (passed byref). 
User Contributed Notes
burnincoldblue at comcast dot net | Oct-28-04 03:56:34  
---|---  
I advise you to be very careful on how you word your script. Improper wording can make your server crash.   
  

