egister_native
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
register_native - Declares a native that other plugins can use. 
Syntax
register_native ( const name[], const handler[], [ style = 0 ] ) 
Type
Native 
Notes
When a plugin uses your native (you should distribute a .inc), the handler will be called with two parameters: the calling plugin id, and the number of parameters.   
  
If you set style=1, the method of parameter passing is a tad more efficient. Instead of "id, numParams", you label the native exactly as how the parameters should, in theory, be sent. Then for each byreference parameter, you call param_convert(num). This is theoretically more efficient but quite hacky. The method was discovered by dJeyL, props to him!   
  
The advantage to keeping style set to 0 is that it more closely resembles the AMX Mod/X module API.
