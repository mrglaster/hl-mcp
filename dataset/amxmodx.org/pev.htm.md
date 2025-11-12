ev
[Fakemeta](http://127.0.0.1:8000/content/index.htm) (fakemeta.inc) 
Description
pev - Returns edict data from an entity. 
Syntax
pev ( index, value, [ ... ] ) 
Type
Native 
Notes
index is the numerical entity index.   
value is the section of the edict_t for retrieval. Consult fakemeta_const.inc for the list of Pev_* types you can use.   
  
To retrieve an integer, supply no extra parameters.   
To retrieve a float, pass a single float by reference.   
To retrieve a string, pass a string array and max length. 
User Contributed Notes
Freecode | Sep-21-04 19:06:02  
---|---  
example on how to use as to comparing to health `    
new health = get_user_health(id);   
//fakemeta way using pev   
new health = pev(id,pev_health);   
   
set_user_health(id,100);   
//fakemeta way using pev   
set_pev(id,pev_health,100);   
  `  
  

