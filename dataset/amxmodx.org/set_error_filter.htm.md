et_error_filter
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
set_error_filter - Allows you to trap error messages that occur in your plugin. 
Syntax
set_error_filter ( const handler[] ) 
Type
Native 
Notes
You can use this to override the debug messages that occur when your plugin causes some sort of runtime error. A plugin can only have one error filter at one time. Subsequent calls to set_error_filter always replace the old filter.   
  
Parameters:   
* handler: The public callback function that should be called when an error occured.   
  
The handler function will be called with these parameters:   
`    
public error_filter(error_code, bool:debugging, message[])   
  `   
* error_code: Specifies the error that occured. This can be one of the AMX_ERR_* values defined in amxconst.inc   
* debugging specifies whether the plugin runs in debug mode   
* message is any message that was sent along with the error   
  
When the handler function returns PLUGIN_HANDLED, the error is blocked from displaying. Returning PLUGIN_CONTINUE lets the error pass the filter.   

