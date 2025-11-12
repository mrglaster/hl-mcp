# Finding Entities (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#p-search)
## Contents
  * [1 Introduction](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#Introduction)
  * [2 Functions](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#Functions)
  * [3 find_ent_by_class](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#find_ent_by_class)
  * [4 find_ent_by_model](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#find_ent_by_model)
  * [5 find_ent_by_owner](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#find_ent_by_owner)
  * [6 find_ent_by_target](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#find_ent_by_target)
  * [7 find_ent_by_tname](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#find_ent_by_tname)
  * [8 find_ent_in_sphere](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#find_ent_in_sphere)
  * [9 find_sphere_class](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#find_sphere_class)
  * [10 Looping](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#Looping)
  * [11 Wrap Up](https://wiki.alliedmods.net/Finding_Entities_\(AMX_Mod_X\)#Wrap_Up)


## Introduction
It is sometimes necessary to find an entity in the world for some reason. For example, you may need to find a button in the world, and then remove it (this example will be covered later). This article will explain how to do so. 
## Functions
There are a number of functions built into AMX Mod X / AMXX Modules that allow you to find entities. For a complete list, please consult this page: [http://www.amxmodx.org/funcwiki.php?search=find_ent&go=search](http://www.amxmodx.org/funcwiki.php?search=find_ent&go=search)
(As of last edit, these are the functions included): 
  * find_ent_by_class
  * find_ent_by_model
  * find_ent_by_owner
  * find_ent_by_target
  * find_ent_by_tname
  * find_ent_in_sphere
  * find_sphere_class


## find_ent_by_class
<Function is included in Engine>
This function allows you to find an entity based on it's classname. All entities have classnames. For example, a player's classname is "player", while a button is either "func_button" or "func_rot_button". 
To find an entity using this, one would simply use the following: 
```
find_ent_by_class(-1,"classname_to_find");
```

Note : Index is -1 because that's the invalid entity index. We start from the invalid one so we can get all the entities, if you start from a different index, all entities with a lower index will be ignored. 
## find_ent_by_model
<Function is included in Engine>
This function can be used to find an entity based on its model. Some entities do not have models, meaning they cannot be found using this method. Also, it is, most of the time, better to use another type of ent finding, as this can be highly inaccurate and be broken by something as simple as a model changing plugin. This function also takes into account the class name, and is generally used more for isolating a certain model from a set of classnames (ex you have 3 grenades, with different models, and want to find 1 of them) 
To find an entity using this, one would use the following: 
```
find_ent_by_model(-1,"classname_to_find","model_to_find")
```

## find_ent_by_owner
<Function is included in Engine>
This function can be used to find an entity based on an owner. For example, if there is a player in the world, and you want to find if he has thrown a grenade out, you would use this and check for "grenade" entities that's owner is the player. Note: planted C4 (in CS) also have "grenade" classname. 
To find an entity using this, one would use the following: 
```
find_ent_by_owner(-1,"classname_to_find",owner_id,0);
```

Notice the last parameter. This is a mode to find in. To see a full list, consult this page: [http://www.amxmodx.org/funcwiki.php?go=func&id=345](http://www.amxmodx.org/funcwiki.php?go=func&id=345)
## find_ent_by_target
<Function is included in Engine>
This function allows one to find an entity based on its target. This function also checks for classname. 
To find an entity using this, one would use the following: 
```
find_ent_by_target(-1,"classname_to_find");
```

## find_ent_by_tname
<Function is included in Engine> This essentially functions the same as find_ent_by_target. 
## find_ent_in_sphere
<Function is included in Engine>
This function can be used to find an entity within a certain distance of another entity. This can be quite handy to, for example, see if a player is around another player, and then deal damage or slap that player. This is effectively a shortcut to using find_ent_by_class and get_distance(_f) together. 
To find an entity using this, one would use the following: 
```
find_ent_in_sphere(-1,location_of_ent_vector,radius_float);
```

## find_sphere_class
This function is probably the most complex of all the find_ent functions. This allows you to find an entity inside a certain radius of another entity, with a certian classname. This is effectively a shortcut to using find_ent_by_class & get_distance & entity_get_string(ent,EV_SZ_classname... or find_ent_in_sphere & entity_get_string(ent,EV_SZ_classname... 
To find an entity using this, one would use the following: 
```
new entlist[513];
find_sphere_class(0,"classname_to_find",radius_float,entlist,512,origin_vector);
```

Also, note that origin_vector and the first parameter (_aroundent) should not both be specified. If _aroundent is specified as 0, origin_vector is used. If origin_vector is not specified, or is 0, then _aroundent is used. 
## Looping
If, for example, one wants to loop one of these, it is quite simple to do so. 
Example: 
```
while((ent = find_ent_by_class(ent,"classname_to_find")) != 0)
{
	// do whatever
}
```

This will find every entity with classname "classname_to_find" and then execute the "// do whatever" code every time it finds one. 
## Wrap Up
For complete usage, please consult the Engine Module page at: [http://www.amxmodx.org/funcwiki.php?go=module&id=3](http://www.amxmodx.org/funcwiki.php?go=module&id=3)
