et_tr
[Fakemeta](http://127.0.0.1:8000/content/index.htm) (fakemeta.inc) 
Description
get_tr - Returns value of tr_member within the trace. 
Syntax
get_tr ( TraceResult:tr_member, [ ... ] ) 
Type
Native 
Notes
Only use this with functions that pass a Trace, such as a TraceLine forward registered with FakeMeta.   
  
With no extra parameters this returns an integer value. With one extra parameter this a returns float or vector value by reference.   

