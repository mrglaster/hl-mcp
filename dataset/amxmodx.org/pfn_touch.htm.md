fn_touch
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
pfn_touch - Called when two entities touch/collide. 
Syntax
pfn_touch ( ptr, ptd ) 
Type
Forward 
Notes
Players will always show up as the touched (ptd).   
  
Returning PLUGIN_HANDLED will block the engine call.
