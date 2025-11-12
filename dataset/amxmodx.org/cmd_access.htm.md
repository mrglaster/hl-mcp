md_access
[Core](http://127.0.0.1:8000/content/index.htm) (amxmisc.inc) 
Description
cmd_access - Checks if a user has access for that command. 
Syntax
cmd_access ( id, level, cid, num ) 
Type
Stock 
Notes
You usually use it like this:   
`   if (!cmd_access(id,level,cid,1))   
    return PLUGIN_HANDLED  `   
  
The last parameter (num) is the number of arguments.   
Note that the first parameter is the command name so if you expect one param set it to 2.   
  
This will automatically print out messages such as "You have no access to that command" and "Usage: <soandso".
