ind_sphere_class
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
find_sphere_class - Returns the number of ents stored in entlist 
Syntax
find_sphere_class ( aroundent, _lookforclassname[], Float:radius, entlist[], maxents, Float:origin[3] = {0.0, 0.0, 0.0} ) 
Type
Native 
Notes
Use to find a specific type of entity classname specify in _lookforclassname) around a certain entity specified in aroundent. All matching ents are stored in entlist. Specify max amount of entities to find in maxents.   
  
If aroundent is 0 its origin is not used, but origin in 6th parameter. Ie, do not specify 6th parameter (origin) if you specified an entity in aroundent.
