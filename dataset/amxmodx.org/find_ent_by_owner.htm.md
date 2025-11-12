ind_ent_by_owner
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
find_ent_by_owner - Finds an entity in the world by owner, returning the index. 
Syntax
find_ent_by_owner ( StartIndex, Classname[], OwnerEntity, [ type ] ) 
Type
Native 
Notes
If none is found, 0 is returned. If starting entity should not be specified, use -1.   
  
Type defaults to 0, it can be set to:   
0: Find by Classname   
1: Find by Target   
2: Find by Target Name
