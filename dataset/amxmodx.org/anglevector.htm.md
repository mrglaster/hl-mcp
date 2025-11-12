nglevector
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
anglevector - Engine function, ANGLEVECTOR. 
Syntax
anglevector ( Float:vector[3], FRU, Float:vReturn[3] ) 
Type
Native 
User Contributed Notes
adrianhenning at sbcglobal dot net | Oct-27-04 14:41:31  
---|---  
It appears that this function operates in the same way as NS2AMX's. Specifically, FRU needs to be one of these values, otherwise vReturn[3] will be an undefined value. In most cases, you want to use ANGLEVECTOR_FORWARD. NOTE: These defines are not present in AMX Mod X as of 0.20 RC6. `    
// ...from ns2amxdefines.inc, by Steve Dudenhoeffer...   
// Used for anglevector()   
#define ANGLEVECTOR_FORWARD      1   
#define ANGLEVECTOR_RIGHT        2   
#define ANGLEVECTOR_UP           3   
  `  
  

