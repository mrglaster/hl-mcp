et_tr
[Fakemeta](http://127.0.0.1:8000/content/index.htm) (fakemeta.inc) 
Description
set_tr - Sets value of tr_member within the trace. 
Syntax
set_tr ( TraceResult:tr_member, [ ... ] ) 
Type
Native 
Notes
Only use this with functions that pass a Trace, such as a TraceLine forward registered with FakeMeta. 
User Contributed Notes
XxAvalanchexX at hotmail dot com | Jan-31-05 04:59:01  
---|---  
Example: `    
public plugin_init()   
{   
   register_forward(FM_TraceLine,"traceline",1);   
}   
   
public traceline(Float:v1[3],Float:v2[3],noMonsters,pentToSkip)   
{   
   if(is_user_connected(pentToSkip) && is_user_alive(pentToSkip))   
   {   
      set_tr(TR_pHit,pentToSkip); // make users shoot themselves   
   }   
}   
  `  
  

