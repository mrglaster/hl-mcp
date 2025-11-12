et_concmd
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_concmd - Gets info about console command. 
Syntax
get_concmd ( index,cmd[],len1,&flags, info[],len2, flag, id = -1 ) 
Type
Native 
Notes
If id is set to 0, then the function returns only server cmds, if positive then it returns only client cmds. In any other case it returns all console commands.
