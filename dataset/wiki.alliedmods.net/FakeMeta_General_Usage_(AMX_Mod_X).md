# FakeMeta General Usage (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#p-search)
## Contents
  * [1 Current FakeMeta and Old](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#Current_FakeMeta_and_Old)
  * [2 About](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#About)
  * [3 Engine vs. FakeMeta](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#Engine_vs._FakeMeta)
  * [4 General Functionality](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#General_Functionality)
  * [5 Entvars](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#Entvars)
  * [6 DLL / Engine Function Usage](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#DLL_.2F_Engine_Function_Usage)
  * [7 Return Values](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#Return_Values)
  * [8 Constants / General](https://wiki.alliedmods.net/FakeMeta_General_Usage_\(AMX_Mod_X\)#Constants_.2F_General)


## Current FakeMeta and Old
FakeMeta used to be an internal mini-metamod inside [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X"). This was removed in 1.50, and now only the module remains. The module is an entirely different concept, which extends [Metamod](https://wiki.alliedmods.net/Metamod "Metamod") HL1 programming powers to scripts. 
## About
FakeMeta is an extremely powerful module for AMX Mod X that effectively allows you to write Metamod plugins in [Pawn](https://wiki.alliedmods.net/Pawn "Pawn"). 
Unlike Engine, FakeMeta uses no CPU if it is not told to do anything (other than to exist). For this reason, it is recommended to use FakeMeta over Engine. There is nothing in Engine that is not in FakeMeta -- while some functionality might be less [abstracted](https://wiki.alliedmods.net/index.php?title=Abstraction&action=edit&redlink=1 "Abstraction \(page does not exist\)"), it is still achievable, and usually with more flexibility. 
## Engine vs. FakeMeta
Comparison between Engine and FakeMeta: 
FakeMeta: 
```
#include <amxmodx>
#include <fakemeta>
 
public plugin_init()
{
	register_plugin("FakeMeta Test","1.0","Hawk552");
 
	register_forward(FM_PlayerPreThink,"PreThink");
}
 
public PreThink(id)
{
	// here you would insert some code
 
	return FMRES_IGNORED;
}
```

Engine: 
```
#include <amxmodx>
#include <engine>
 
public plugin_init()
{
	register_plugin("Engine Test","1.0","Hawk552");
}
 
public client_PreThink(id)
{
	// here you would insert some code
 
	return;
}
```

The "return FMRES_IGNORED" section will be covered later on this page. 
## General Functionality
FakeMeta also allows you to do other things, such as retrieve private data (using pev, set_pev / get_pdata_int, get_pdata_float, get_pdata_string, set_pdata_int, set_pdata_float, set_pdata_string), forcing DLL functions to be executed, as well as call Engine (not the module) functions. 
## Entvars
It is easy to read [entvars](https://wiki.alliedmods.net/index.php?title=Entvars_\(Half-Life_1\)&action=edit&redlink=1 "Entvars \(Half-Life 1\) \(page does not exist\)") in FakeMeta, however it can sometimes cause problems if not done correctly (which is why Engine is more commonly used). Entvars are variables in a player's [edict](https://wiki.alliedmods.net/index.php?title=Edicts_\(Half-Life_1\)&action=edit&redlink=1 "Edicts \(Half-Life 1\) \(page does not exist\)") structure (an edict is the basis for an entity). 
Here is an example of how to retrieve the armor entvar from an entity in FakeMeta: 
```
#include <amxmodx>
#include <fakemeta>
 
public plugin_init()
{
	register_plugin("FakeMeta Test","1.0","Hawk552");
 
	register_forward(FM_PlayerPreThink, "PreThink");
}
 
public PreThink(id)
{
	new value = pev(id,pev_armorvalue); // gets armor from client/entity
 
	client_print(id,print_chat,"%i",value); // prints armor value to client
 
	return FMRES_IGNORED;
}
```

## DLL / Engine Function Usage
In DLLs and the Engine, there are functions that are called when certain events happen. These can be forced to be called through FakeMeta. Here is a general example: 
```
#include <amxmodx>
#include <fakemeta>
 
public plugin_init()
{
	register_plugin("FakeMeta Test","1.0","Hawk552");
 
	register_forward(FM_PlayerPreThink,"PreThink");
}
 
public PreThink(id)
{
	dllfunc(DLLFunc_RegisterEncoders);
 
	return FMRES_IGNORED;
}
```

Refer to the end of the line while viewing the DLLFunc and EngFunc sections, as there is usually some description of paramaters, such as _edict_t *p_Entity_ or _void_. _void_ generally refers to no parameters, while _edict_t *p_Entity_ means the entity id, so the first parameter in the function would be the entity to call the function onto. 
## Return Values
There are 4 return values in FakeMeta: 
  * FMRES_HANDLED --> Something was done in this function, but call the one in the DLL / Engine anyways.
  * FMRES_SUPERCEDE --> Prevent function in DLL / Engine from being called.
  * FMRES_IGNORED --> Call original function.
  * FMRES_OVERRIDE --> Call original function, but change return value.


## Constants / General
A list of general constants and usage can be found on this page: [http://www.amxmodx.org/funcwiki.php?go=module&id=16](http://www.amxmodx.org/funcwiki.php?go=module&id=16)
