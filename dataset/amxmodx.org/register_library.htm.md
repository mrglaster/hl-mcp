egister_library
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
register_library - Registers your plugin as a library. 
Syntax
register_library ( const name[] ) 
Type
Native 
Notes
You can put #pragma library <name in your include files, and plugins that use your include without loading your plugin will get a nice error message.   
  
This native technically just makes the Core think your plugin is a module; this is part of the "auto-module" system where failed plugins automatically know what modules they need.
