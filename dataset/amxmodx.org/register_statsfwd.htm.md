egister_statsfwd
[DoDX](http://127.0.0.1:8000/content/index.htm) (dodx.inc) 
Description
register_statsfwd - Use this function to register forwards 
Syntax
register_statsfwd ( forward_index ) 
Type
Native 
Notes
For forwards list check dodx.inc file   
example :   
  
public plugin_init() {   
...   
register_statsfwd(XMF_DAMAGE)   
...   
}   
  
This will register client_damage(...) forward   

