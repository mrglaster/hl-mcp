egister_forward
[Fakemeta](http://127.0.0.1:8000/content/index.htm) (fakemeta.inc) 
Description
register_forward - Registers a forward in the HL engine 
Syntax
register_forward ( forwardType, callback[], [ post = 0 ] ) 
Type
Native 
Notes
This will hook a function in the HL engine or mod DLL and forward it to a function in an AMXx plugin.   
  
forwardType is a forward identifer type, such as FM_PrecacheModel, which selects the function to hook.   
callback[] is a string which identifies the public function to call when the forward is hooked.   
  
If post is set to 1, the function is a "POST" function in metamod, which means that it is called AFTER the engine has called the original. This also means you cannot block the original function.   
  
Note that using this native incorrectly can crash the Half-Life engine. Each forward should exactly match the parameters in the fakemeta_const.inc file. To find parameter types from original HL engine functions, use this chart:   
  
const char * = str[]   
int = num   
float = Float:flt   
float * = Float:vFlt[3]   
  
To return data inside the hooked call, use [forward_return](http://127.0.0.1:8000/content/forward_return.htm).   
To block a function as you would in Metamod, use these return values:   
  
#define FMRES_HANDLED 2   
#define FMRES_SUPERCEDE 4   
#define FMRES_IGNORED 1   
#define FMRES_OVERRIDE 3   
  

