s_get_build
[NS](http://127.0.0.1:8000/content/index.htm) (ns.inc) 
Description
ns_get_build - Returns built/unbuilt structures. 
Syntax
ns_get_build ( classname[], [ builtOnly = 1 ], [ Number = 0 ] ) 
Type
Native 
Notes
If builtOnly is 1 (default): Only fully built structures are counted.   
  
If builtOnly is 0: Any structure meeting the classname is counted.   
  
If Number is 0 (default): The total number of matching structures is returned.   
  
If Number is any other value: The index of the #th matching structure is returned.
