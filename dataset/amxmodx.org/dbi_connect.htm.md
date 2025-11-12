bi_connect
[SQL](http://127.0.0.1:8000/content/index.htm) (dbi.inc) 
Description
dbi_connect - Connects to a mysql database. 
Syntax
dbi_connect ( host[], user[], pass[], dbname[], [ error[] = "", maxLength = 0 ] ) 
Type
Native 
Notes
Return type is Sql, which means you have to declare your variable as Sql:name, just as you declare a float as Float:name.   
  
Returns a resource handle greater than 0 on success.   
  
If an error was found, it is stored into error[] for a maximum of len characters.
