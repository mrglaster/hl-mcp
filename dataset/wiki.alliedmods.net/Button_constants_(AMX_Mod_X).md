# Button constants (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Button_constants_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Button_constants_\(AMX_Mod_X\)#p-search)
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/Ru:Button_constants_\(AMX_Mod_X\) "Ru:Button constants \(AMX Mod X\)") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/index.php?title=Zh_cn:Button_constants_\(AMX_Mod_X\)&action=edit&redlink=1 "Zh cn:Button constants \(AMX Mod X\) \(page does not exist\)") |   
  

## Usage
Button constants are generally used to determine when an entity is doing a certain action, such as jumping, attacking, or moving. This is used because +/- commands cannot be hooked by the HL engine (if they are made by the HL engine). 
For example, this would work: 
```
register_concmd("+explode","explode");
```

However this would not: 
```
register_concmd("+attack","hook_attack");
```

## Constants
A full list of constants can be found [here](http://amxmodx.org/api/hlsdk_const#pev-entity-pev-button-or-pev-entity-pev-oldbuttons-values/). 
## Implementation
If, for example, it is desired to check when a player is attacking, one would use the following: 
```
#include <amxmodx>
#include <engine>
 
public plugin_init()
{
	register_plugin("Attack Test","1.0","Hawk552");
}
 
public client_PreThink(id)
{
	if(entity_get_int(id,EV_INT_BUTTON) & IN_ATTACK)
	{
		// do something
	}
}
```

Notice how this uses the & operator, rather than the && operator. This is because a bit value is returned, and the & operator checks if a bit value is contained in another bit value. 
To set an entity's button, the same type of idea can be implemented: 
```
#include <amxmodx>
#include <engine>
 
public plugin_init()
{
	register_plugin("Attack Test","1.0","Hawk552");
}
 
public client_PreThink(id)
{
	entity_set_int(id,EV_INT_button,IN_ATTACK);
}
```

This sets the client's attack flag to _on_ every time a frame is rendered. 
To get an entity's buttons, and then ommit a certain button, one would use the following: 
```
#include <amxmodx>
#include <engine>
 
public plugin_init()
{
	register_plugin("Attack Test","1.0","Hawk552");
}
 
public client_PreThink(id)
{
	entity_set_int(id,EV_INT_button,entity_get_int(id,EV_INT_button) & ~IN_ATTACK);
}
```

Say, for example, during a certain time, the client is jumping and attacking at the same time. In this case, the entity_get_int(id,EV_INT_button) function would return IN_ATTACK and IN_JUMP. Using the ~ operator removes the certain bit value, making it into merely IN_JUMP. 
There are many more ways to use button constants, and not all must be used on players. They are simply more commonly implemented when dealing with players. 
