egister_plugin
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
register_plugin - Sets a plugin's info 
Syntax
register_plugin ( const plugin_name[], const version[], const author[] ) 
Type
Native 
Notes
This registers a plugin into the plugin list.   
  
Example:   
`    
#define PLUGIN_NAME "Admin Abuse"   
#define PLUGIN_VERSION "1.00"   
#define PLUGIN_AUTHOR "The Man"   
   
public plugin_init()   
  
   register_plugin(PLUGIN_NAME, PLUGIN_VERSION, PLUGIN_AUTHOR)   
}   
  `
