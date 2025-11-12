# OrpheuGetFunctionFromMonster
#### Syntax
```
native OrpheuFunction:OrpheuGetFunctionFromMonster(id, const libFunctionName[], const libClassName[])
```

#### Usage
id | ```The id of a monster from monstermod```
---|---
libFunctionName | ```The library function name as it is in the file created to define the function```
libClassName | ```The library function name as it is in the file created to define the function```
#### Description
```
Retrieves a handler to a function given the id of a monster of monstermod, the function name and the classname
This function is a virtual function (a function defined in abase class and implemented
differently by each extender class)
For example: every class that extends CBaseEntity has a Spawn function. That function is defined in CBaseEntity
and implemented differently by each class derived from CBaseEntity

This function goes against the spirit of orpheu of hardcoding the less possible but without it would be much
more complex to use virtual functions
```

#### Return
```
A handler to the function
```


This code is a part of orpheu.inc. To use this code you should include orpheu.inc as ```#include <orpheu>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. Orpheu is outdated and not recommended for use, so use Include at your own risk. 