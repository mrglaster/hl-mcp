# Scripting Cvars (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#p-search)
[CVARs](https://wiki.alliedmods.net/index.php?title=CVARs&action=edit&redlink=1 "CVARs \(page does not exist\)"), or Console VARiables, are an easy and efficient way to store configurable variables on the server. Half-Life 1 supports both server-side cvars and client-side cvars. Internally, cvars are stored as both a float and a string. CVARs can be used for easy access outside the plugin. Valid example would be : Storing Weapon Knock back in a CVAR then editing it via configurable files. 
## Contents
  * [1 Server-Side](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Server-Side)
    * [1.1 Getting Values](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Getting_Values)
    * [1.2 Setting Value](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Setting_Value)
    * [1.3 Flags](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Flags)
  * [2 Client Side CVARs](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Client_Side_CVARs)
    * [2.1 Getting](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Getting)
    * [2.2 Setting](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Setting)
    * [2.3 Locking](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Locking)


## Server-Side
To create a cvar, use `register_cvar`. 
```
register_cvar(const name[],const string[],flags = 0,Float:fvalue = 0.0);
```

Note: The last parameter is for backwards compatibility only, and serves no purpose in AMXx. It is recommended you register CVARs during [plugin_init](https://wiki.alliedmods.net/index.php?title=Core_Forwards_\(AMX_Mod_X\)&action=edit&redlink=1 "Core Forwards \(AMX Mod X\) \(page does not exist\)"), so that other plugins may alter them at [plugin_cfg](https://wiki.alliedmods.net/index.php?title=Core_Forwards_\(AMX_Mod_X\)&action=edit&redlink=1 "Core Forwards \(AMX Mod X\) \(page does not exist\)"). 
  * Parameters: 
    * name[] : The name of the CVAR you want to register
    * string[] : The default value of the CVAR
    * flags : See [Cvars (AMX Mod X)](https://wiki.alliedmods.net/Scripting_Cvars_\(AMX_Mod_X\)#Flags).


### Getting Values
```
/* Gets a cvar float. */
Float:get_cvar_float(const cvarname[]);

/* Gets a cvar integer value. */
get_cvar_num(const cvarname[]);

/* Reads a cvar value. */
get_cvar_string(const cvarname[],output[],iLen);

```

### Setting Value
```
/* Sets a cvar to given value. */
set_cvar_string(const cvar[],const value[]);

/* Sets a cvar to given float. */
set_cvar_float(const cvar[],Float:value);

/* Sets a cvar with integer value. */
set_cvar_num(const cvarname[],value);

```

### Flags
These flags can be used for the third parameter in the `register_cvar` native: 
```
#define	FCVAR_ARCHIVE		1	/* set to cause it to be saved to vars.rc */
#define	FCVAR_USERINFO		2	/* changes the client's info string */
#define	FCVAR_SERVER		4	/* notifies players when changed */
#define FCVAR_EXTDLL		8	/* defined by external DLL */
#define FCVAR_CLIENTDLL		16	/* defined by the client dll */
#define FCVAR_PROTECTED		32	/* It's a server cvar, but we don't send the data since it's a password, etc.  Sends 1 if it's not bland/zero, 0 otherwise as value */
#define FCVAR_SPONLY		64	/* This cvar cannot be changed by clients connected to a multiplayer server. */
#define FCVAR_PRINTABLEONLY	128	/* This cvar's string cannot contain unprintable characters ( e.g., used for player name etc ). */
#define FCVAR_UNLOGGED		256	/* If this is a FCVAR_SERVER, don't log changes to the log file / console if we are creating a log */

```

You can alter these flags dynamically, using the cvar flag natives: 
```
/* Returns a cvar flags. */
get_cvar_flags(const cvar[]);

/* Sets a cvar flags (not allowed for amx_version,
* fun_version and sv_cheats cvars). */
set_cvar_flags(const cvar[],flags);

/* Removes a cvar flags (not allowed for amx_version,
* fun_version and sv_cheats cvars). */
remove_cvar_flags(const cvar[],flags = -1);

```

## Client Side CVARs
Client side cvars cannot be created in Half-Life 1. The cvar must exist in advance. Furthermore, since it must be retrieved or set over the network, knowing the value at a given point in time is impossible. You can, however, query a client for a cvar and get an asynchronous response, and use client_cmd to set a new value if necessary. 
### Getting
Recently, VALVE added a client CVAR checking interface, which has been added to AMX Mod X: 
```
// Dispatches a client cvar query
//  id: Player id
//  cvar: cvar name
//  resultFunc: public handler function
//  paramLen + params: optional array parameter
// resultFunc looks like:
//  public callbackCvarValue(id, const cvar[], const value[])
// or if you use the optional parameter:
//  public callbackCvarValue(id, const cvar[], const value[], const param[])
query_client_cvar(id, const cvar[], const resultFunc[], paramlen=0, const params[] = "");

```

This native may appear daunting, but it is actually quite simple; the first parameter is the player, the second the cvar, the third the function called which will contain the client CVAR, and the last two are for allowing the passage of strings. 
If you wish to get an array or strting back, simply put the length you want it, and fill params will a value. Then, in your return function, you will receive an array. 
### Setting
Setting a client side CVAR is easy; execute a new value onto the client: 
`client_cmd(player_id,"cvar value")`
### Locking
Since the client can change cvar values back as soon as they're set, it might be necessary to lock them. Since alias's are executed before cvars, you can create an alias of the same name of the cvar, thus locking the cvar: 
```
//CVAR: cvar_ex.
client_cmd(player_id,"cvar_ex 1")
client_cmd(player_id,";alias cvar_ex")
```

Now the cvar cannot be changed by the player or the server; it is locked. 
