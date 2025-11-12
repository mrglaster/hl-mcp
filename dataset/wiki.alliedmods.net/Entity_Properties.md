# Entity Properties
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Entity_Properties#mw-head), [search](https://wiki.alliedmods.net/Entity_Properties#p-search)
This article is a brief introduction into Half-Life 2 entity properties. 
## Contents
  * [1 Introduction](https://wiki.alliedmods.net/Entity_Properties#Introduction)
  * [2 Network Properties](https://wiki.alliedmods.net/Entity_Properties#Network_Properties)
    * [2.1 Network Variables](https://wiki.alliedmods.net/Entity_Properties#Network_Variables)
    * [2.2 Send Properties](https://wiki.alliedmods.net/Entity_Properties#Send_Properties)
    * [2.3 Send Tables](https://wiki.alliedmods.net/Entity_Properties#Send_Tables)
    * [2.4 Server Classes](https://wiki.alliedmods.net/Entity_Properties#Server_Classes)
  * [3 Data Maps](https://wiki.alliedmods.net/Entity_Properties#Data_Maps)
  * [4 Enumeration](https://wiki.alliedmods.net/Entity_Properties#Enumeration)
    * [4.1 Server Classes](https://wiki.alliedmods.net/Entity_Properties#Server_Classes_2)
    * [4.2 Send Properties](https://wiki.alliedmods.net/Entity_Properties#Send_Properties_2)
    * [4.3 Datamap Properties](https://wiki.alliedmods.net/Entity_Properties#Datamap_Properties)
  * [5 SourceMod Commands](https://wiki.alliedmods.net/Entity_Properties#SourceMod_Commands)
  * [6 External Links](https://wiki.alliedmods.net/Entity_Properties#External_Links)


# Introduction
**In layman's terms:** Entity properties are named variables attached to entities. Each variable is located at a specific offset from the entity. For example, CS:S player entities have a variable called "m_iAccount" which is offset 3,608 bytes from every player in memory. These variables, as well as their offsets, are enumerable at run-time. They are not the same as KeyValues inputs, which are designed to accept information from maps. Entity properties are the raw, internal data that comprises an entity. 
**In C++ terms:** Entity properties are named, retrievable properties that represent a certain data structure specific to an entity instance. They are usually tied to variables of CBaseEntity and its derivatives. Each named property is tied to, among other pieces of information, an offset from the `this` pointer of the entity. This means that server-side developers can easily decompose entity information, because the variable names and offsets are enumerable. 
The information here is intended for server-side plugin developers who are learning, programming, or reverse engineering a mod that does not nicely expose API for modifying entities. Mod developers should use the [Valve Wiki](http://developer.valvesoftware.com/). 
There are two main property types for Source entities: 
  * **SendProps** : These are properties designed for networking. Changes are mirrored to clients via the Source engine and RecvProps.
  * **DataMaps** : These are properties designed for saving and restoring an entity. Unlike SendProps, they are not necessarily networkable, and they are more mod specific.


  

# Network Properties
Network properties deal with properties that must be transmitted over the network. There are four pieces to this: 
  * Network variables, which handle marking offsets in memory as changed.
  * Send properties, which describe how the memory/data at the offset should be networked.
  * Send tables, also called data tables, which contain lists of send properties.
  * Server classes, which contain all of the send tables an entity needs for networking.


Since correct networking is crucial to client/server communication, the send table hierarchy must be the same between the server and the client. Otherwise, the client will not be able to connect to the server. 
## Network Variables
The purpose of network variables is to notify the engine of which entities, and which offsets in those entities, need to be re-transmitted over the network because they have changed. 
**Important Headers** : `public/networkvar.h`, `public/edict.h`
Network variables are simple, operator-overloading macros, which box the original value type. This is to detect state changes. When m_fOnTarget is changed via normal means (for example, using C++ operators and not something like `memcpy`), it will trigger a function called `NetworkStateChanged()` in the entity. This state change can be global (resends the entire entity) or offset specific (only transmits as many bits as needed). 
The order of operations is usually similar to: 
  1. Code, like the following, is executed: ```
m_fOnTarget = false;
```

  2. This assignment triggers `::NetworkStateChanged(address)` in `CBaseEntity` or its derived class.
  3. This calls `CServerNetworkProperty::NetworkStateChanged(offset_from_this)`
  4. This calls `edict_t::StateChanged(offset_from_baseent)` (entities are tied to edicts)
  5. If the entity has had more than 19 offsets changed, or more than 100 entities have changed, the entire entity is marked for retransmission. 
  6. Otherwise, its changed offset is added to the global change offset table.


An example of a network variable being declared looks like below, from `dlls/player.cpp`: 
```
	CNetworkVar( bool, m_fOnTarget );		//Is the crosshair on a target?
```

## Send Properties
While network properties are for notifying the engine of changes, send properties tell the engine exactly how to deal with those changes. 
**Important Headers** : `public/dt_send.h`, `public/dt_shared.h`, `public/dt_common.h`
Send properties enumerate the following pieces of information about each network offset: 
  * A `SendPropType` value (Int, Float, Vector, String, Array, or Data Table).
  * The number of bits to transmit.
  * The name of the property (usually, the same as the variable name).
  * Transmission flags (such as, whether it is signed or unsigned).
  * The offset from the CBaseEntity pointer at which this variable lives.


An example of a SendProp being declared looks like below, from `dlls/player.cpp`: 
```
SendPropInt ( SENDINFO( m_fOnTarget ), 2, SPROP_UNSIGNED ),
```

This declares an unsigned send property that only transmits two bits. 
## Send Tables
Send tables, also called _data tables_ , encapsulate a set of related send properties. Send tables can be nested; if there is a send property that includes a send table, the tables will effectively be merged. 
**Important Headers** : `public/dt_send.h`
Send tables have explicit names. For example the following line from `dlls/player.cpp` begins a send table named `DT_PlayerState`: 
```
BEGIN_SEND_TABLE_NOBASE(CPlayerState, DT_PlayerState)
```

This particular send table is then linked into `DT_BasePlayer` via: 
```
SendPropDataTable(SENDINFO_DT(pl), &REFERENCE_SEND_TABLE(DT_PlayerState), SendProxy_DataTableToDataTable),
```

## Server Classes
Server classes are at the highest level of the networking chain. Each server class has: 
  * A unique name (a `ClassName` as opposed to an entity's `Classname`).
  * A root send table.
  * A pointer to the next server class in the chain.


**Important Headers** : `public/server_class.h`
While server classes are not related, they are globally linked via a constructor - this is simply to make development easier. The engine retrieves the first server class pointer via `IServerGameDLL::GetAllServerClasses()`. Using this pointer, the engine can find every single server class, and thus all send tables in the tree, and likewise, all send properties in each table. 
Usually, each major CBaseEntity derivation contains a server class. For example, for Counter-Strike:Source, there is a `CCSPlayer` server class. Its major hierarchy looks roughly like: 
  * CCSPlayer 
    * DT_CSPlayer 
      * DT_BasePlayer 
        * DT_BaseCombatCharacter 
          * DT_BaseFlex 
            * DT_BaseAnimatingOverlay 
              * DT_BaseAnimating 
                * DT_BaseEntity


Although this is a recursive tree, the properties themselves are all linear. This means, that all send properties under CCSPlayer are all offsets to anything matching a CCSPlayer. 
Because server classes can be enumerated without the instantiation of a given object/entity, send property lookup can be resolved at load time. Even if it needs to be done at run-time, it can be easily optimized given this linear structure. 
# Data Maps
Data maps are properties which are enumerated for save/restore mechanisms. They are less complicated than send properties, but more mod-specific. 
**Important Headers** : `public/datamap.h`
Data maps are encapsulated in a structure called `datamap_t`. This structure contains the following information: 
  * An array of `typedescription_t` structures.
  * A string name.
  * A link to a parent data map, if any.


The `typedescription_t` structure declares one property. It contains: 
  * A `fieldtype_t` data type, which has types such as `FIELD_INTEGER` and `FIELD_STRING`
  * A field name, which will usually be the same as the variable name.
  * An offset from the entity pointer to where this data lives.


Data maps can be recursive trees like send tables, since a field can contain another data map. However, there is no known or documented method of easily extracting all data maps. This means that lookup can only be done once an instance to a given entity is known, relying on `CBaseEntity::GetDataDescMap`. 
However, CBaseEntity is ultimately mod specific. Even if it's rare that its position in the virtual table will change, care should be taken to ensure cross-mod compatibility. It is incorrect to assume that calling this function will result in the same behaviour on every mod. 
An example of a data map being declared can be found in `dlls/player.cpp`: 
```
BEGIN_SIMPLE_DATADESC( CPlayerState )
	// DEFINE_FIELD( netname, FIELD_STRING ),  // Don't stomp player name with what's in save/restore
	DEFINE_FIELD( v_angle, FIELD_VECTOR ),
```

  

# Enumeration
## Server Classes
Server classes are easily enumerable. Here is an example function: 
```
/**
 * Searches for a named Server Class.
 *
 * @param name		Name of the top-level server class.
 * @return 		Server class matching the name, or NULL if none found.
 */
ServerClass *UTIL_FindServerClass(const char *name)
{
	ServerClass *pClass = server->GetAllServerClasses();
	while (pClass)
	{
		if (strcmp(pClass->m_pNetworkName, name) == 0)
		{
			return pClass;
		}
		pClass = pClass->m_pNext;
	}
	return NULL;
}
```

## Send Properties
Full send table enumeration requires recursion. An example function below recurses through all properties and sub-table properties of a table. 
```
/**
 * Recursively looks through a send table for a given named property.
 *
 * @param pTable	Send table to browse.
 * @param name		Property to search for.
 * @return 		SendProp pointer on success, NULL on failure.
 */
SendProp *UTIL_FindSendProp(SendTable *pTable, const char *name)
{
	int count = pTable->GetNumProps();
	SendTable *pTable;
	SendProp *pProp;
	for (int i=0; i<count; i++)
	{
		pProp = pTable->GetProp(i);
		if (strcmp(pProp->GetName(), name) == 0)
		{
			return pProp;
		}
		if (pProp->GetDataTable())
		{
			if ((pProp=UTIL_FindSendProp(pProp->GetDataTable(), name)) != NULL)
			{
				return pProp;
			}
		}
	}
 
	return NULL;
}
```

An example usage of both of these functions might look like: 
```
/**
 * Sets a player's health.
 *
 * @param edict		Player's edict.
 * @param health	Health to set.
 */
void SetPlayerHealth(edict_t *edict, int health)
{
	static unsigned int offset = 0;
 
	if (!offset)
	{
		ServerClass *sc = UTIL_FindServerClass("CBasePlayer");
		SendProp *pProp = UTIL_FindSendProp(sc->m_pTable, "m_iHealth");
		offset = pProp->GetOffset();
	}
 
	IServerUnknown *pUnknown = (IServerUnknown *)edict->GetUnknown();
	if (!pUnknown)
	{
		return;
	}
 
	CBaseEntity *pEntity = pUnknown->GetBaseEntity();
	*(int *)((char *)pEntity + offset) = health;
}
```

## Datamap Properties
Here is an example of a function for searching datamaps for a given property. 
```
/**
 * Finds a named offset in a datamap.
 *
 * @param pMap		Datamap to search.
 * @param name		Name of the property to find.
 * @return		Offset of a data map property, or 0 if not found.
 */
unsigned int UTIL_FindInDataMap(datamap_t *pMap, const char *name)
{
	while (pMap)
	{
		for (int i=0; i<pMap->dataNumFields; i++)
		{
			if (pMap->dataDesc[i].fieldName == NULL)
			{
				continue;
			}
			if (strcmp(name, pMap->dataDesc[i].fieldName) == 0)
			{
				return pMap->dataDesc[i].fieldOffset[TD_OFFSET_NORMAL];
			}
			if (pMap->dataDesc[i].td)
			{
				unsigned int offset;
				if ((offset=UTIL_FindInDataMap(pMap->dataDesc[i].td, name)) != 0)
				{
					return offset;
				}
			}
		}
		pMap = pMap->baseMap;
	}
 
	return 0; 
}
```

Now we can rewrite the `SetPlayerHealth` function using data maps: 
```
/**
 * Sets a player's health.
 *
 * @param edict		Player's edict.
 * @param health	Health to set.
 */
void SetPlayerHealth(edict_t *edict, int health)
{
	static unsigned int offset = 0;
 
	IServerUnknown *pUnknown = (IServerUnknown *)edict->GetUnknown();
	if (!pUnknown)
	{
		return;
	}
 
	CBaseEntity *pEntity = pUnknown->GetBaseEntity();
 
	if (!offset)
	{
		offset = UTIL_FindInDataMap(pEntity->GetDataDescMap(), "m_iHealth");
	}
 
	*(int *)((char *)pEntity + offset) = health;
}
```

  

# SourceMod Commands
SDKTools provides two commands for dumping netprops: 
  * `sm_dump_netprops <file>` - Dumps network properties to a named text file (in the mod folder).
  * `sm_dump_netprops_xml <file>` - Dumps network properties to a named text file in XML format (in the mod folder).


  

# External Links
  * [Sample CS:S Network Property Dump](http://www.bailopan.net/table_dump.txt)
  * [Sample TF Network Property Dump](http://www.bailopan.net/tf_netprops.txt)


