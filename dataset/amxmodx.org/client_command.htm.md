lient_command
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
client_command - Called when a client sends a command. 
Syntax
client_command ( id ) 
Type
Forward 
Notes
Called on ClientCommand().   
  
id is a player index from 1 to 32.   
  
You can retrieve the command and its parameters with [read_argv](http://127.0.0.1:8000/content/read_argv.htm), [read_args](http://127.0.0.1:8000/content/read_args.htm), and [read_argc](http://127.0.0.1:8000/content/read_argc.htm).   

