egister_touch
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
register_touch - Registers a touch action to a function. 
Syntax
register_touch ( Toucher[], Touched[], function[] ) 
Type
Native 
Notes
If Toucher or Touched is "*" or "", then it is a wildcard for any classname. Otherwise, you can register specific touches like this:   
  
` register_touch("my_entity", "player", "myent_touch")   
   
public myent_touch(pToucher, pTouched)   
  
}   
  `   
  
This is a blocking forward (PLUGIN_HANDLED will block the operation).   

