lugin_natives
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
plugin_natives - Called when register_native can be used. 
Syntax
plugin_natives ( ) 
Type
Forward 
Notes
This forward is called immediately after the plugin is initialized in memory, much like the deprecated plugin_modules was.   
  
It is safe to use only [register_native](http://127.0.0.1:8000/content/register_native.htm) and [register_library](http://127.0.0.1:8000/content/register_library.htm) here.
