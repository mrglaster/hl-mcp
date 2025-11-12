# FakeMeta Functions Detailed Descriptions
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#mw-head), [search](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#p-search)
## Contents
  * [1 Point Functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Point_Functions)
    * [1.1 EngFunc_PointContents](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_PointContents)
      * [1.1.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage)
    * [1.2 EngFunc_GetBonePosition](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_GetBonePosition)
      * [1.2.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_2)
      * [1.2.2 Useful Stocks](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Useful_Stocks)
        * [1.2.2.1 get_bone_hitgroup](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#get_bone_hitgroup)
        * [1.2.2.2 find_closest_bone_to_gunshot](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#find_closest_bone_to_gunshot)
  * [2 Messaging Functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Messaging_Functions)
    * [2.1 EngFunc_MessageBegin](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_MessageBegin)
      * [2.1.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_3)
  * [3 Entity Search Functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Entity_Search_Functions)
    * [3.1 EngFunc_FindEntityInSphere](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_FindEntityInSphere)
      * [3.1.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_4)
    * [3.2 EngFunc_EntitiesInPVS](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_EntitiesInPVS)
      * [3.2.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_5)
    * [3.3 EngFunc_FindEntityByString](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_FindEntityByString)
      * [3.3.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_6)
    * [3.4 EngFunc_FindClientInPVS](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_FindClientInPVS)
      * [3.4.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_7)
      * [3.4.2 Notes](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Notes)
  * [4 Trace Functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Trace_Functions)
    * [4.1 EngFunc_TraceLine](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_TraceLine)
      * [4.1.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_8)
      * [4.1.2 Other Traceline functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Other_Traceline_functions)
      * [4.1.3 Useful Stocks](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Useful_Stocks_2)
        * [4.1.3.1 is_wall_between_points](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#is_wall_between_points)
      * [4.1.4 Extra Info](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Extra_Info)
    * [4.2 EngFunc_TraceTexture, DLLFunc_PM_FindTextureType](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_TraceTexture.2C_DLLFunc_PM_FindTextureType)
      * [4.2.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_9)
      * [4.2.2 Notes](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Notes_2)
    * [4.3 EngFunc_TraceModel](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_TraceModel)
      * [4.3.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_10)
      * [4.3.2 Extra Info](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Extra_Info_2)
    * [4.4 EngFunc_TraceToss](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_TraceToss)
      * [4.4.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_11)
      * [4.4.2 Example](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Example)
  * [5 Model/Decal/Texture Functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Model.2FDecal.2FTexture_Functions)
    * [5.1 EngFunc_SetModel](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_SetModel)
      * [5.1.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_12)
      * [5.1.2 Engine Alternative](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Engine_Alternative)
    * [5.2 EngFunc_ModelIndex](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_ModelIndex)
      * [5.2.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_13)
    * [5.3 EngFunc_ModelFrames](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_ModelFrames)
      * [5.3.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_14)
    * [5.4 EngFunc_DecalIndex](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_DecalIndex)
      * [5.4.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_15)
      * [5.4.2 Engine alternative](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Engine_alternative_2)
    * [5.5 EngFunc_AnimationAutomove](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_AnimationAutomove)
      * [5.5.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_16)
  * [6 Entity/Global Functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Entity.2FGlobal_Functions)
    * [6.1 EngFunc_NumberOfEntities](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_NumberOfEntities)
      * [6.1.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_17)
      * [6.1.2 Engine alternative](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Engine_alternative_3)
    * [6.2 EngFunc_SetSize](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_SetSize)
      * [6.2.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_18)
      * [6.2.2 Engine alternative](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Engine_alternative_4)
    * [6.3 EngFunc_SetOrigin](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_SetOrigin)
      * [6.3.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_19)
      * [6.3.2 Engine alternative](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Engine_alternative_5)
    * [6.4 EngFunc_MoveToOrigin](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_MoveToOrigin)
      * [6.4.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_20)
      * [6.4.2 Caveats](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Caveats)
  * [7 Visibility Functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Visibility_Functions)
    * [7.1 EngFunc_CheckVisibility](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_CheckVisibility)
      * [7.1.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_21)
  * [8 Other Functions](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Other_Functions)
    * [8.1 EngFunc_PrecacheModel](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_PrecacheModel)
      * [8.1.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_22)
    * [8.2 EngFunc_PrecacheSound](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_PrecacheSound)
      * [8.2.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_23)
    * [8.3 EngFunc_AlertMessage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_AlertMessage)
      * [8.3.1 Usage](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#Usage_24)


## Point Functions
### EngFunc_PointContents
This function checks an origin and gives us information of its whearabouts. 
The constants that this function returns are these: 
```
#define	CONTENTS_EMPTY                  -1
#define	CONTENTS_SOLID                  -2
#define	CONTENTS_WATER                  -3
#define	CONTENTS_SLIME                  -4
#define	CONTENTS_LAVA                   -5
#define	CONTENTS_SKY                    -6
#define	CONTENTS_ORIGIN                 -7          // Removed at csg time
#define	CONTENTS_CLIP                   -8          // Changed to contents_solid
#define	CONTENTS_CURRENT_0              -9
#define	CONTENTS_CURRENT_90             -10
#define	CONTENTS_CURRENT_180            -11
#define	CONTENTS_CURRENT_270            -12
#define	CONTENTS_CURRENT_UP             -13
#define	CONTENTS_CURRENT_DOWN           -14
#define	CONTENTS_TRANSLUCENT            -15
#define	CONTENTS_LADDER                 -16
#define	CONTENT_FLYFIELD                -17
#define	CONTENT_GRAVITY_FLYFIELD        -18
#define	CONTENT_FOG                     -19

```

#### Usage
```
static Float:origin[3]
static result
result = engfunc(EngFunc_PointContents, origin)
// if for example result is CONTENTS_SKY
// then the origin that we see is in the sky we can for example use this to see where a player is aming if he is aiming at sky this will be the result!
```

### EngFunc_GetBonePosition
[![](https://wiki.alliedmods.net/images/PlayerSkeleton.jpg)](https://wiki.alliedmods.net/File:PlayerSkeleton.jpg)
This image shows the locations of the bones, they are marked through blue points. The red point is the player origin.
This function allows to get the bone positions of an entity. This is best used on getting specific player origin points. 
These are the bones that a player has: 
```
Bone 1 Name:  "Bip01"
Bone 2 Name:  "Bip01 Pelvis"
Bone 3 Name:  "Bip01 Spine"
Bone 4 Name:  "Bip01 Spine1"
Bone 5 Name:  "Bip01 Spine2"
Bone 6 Name:  "Bip01 Spine3"
Bone 7 Name:  "Bip01 Neck"
Bone 8 Name:  "Bip01 Head"
Bone 9 Name:  "Bone01"
Bone 10 Name: "Bip01 L Clavicle"
Bone 11 Name: "Bip01 L UpperArm"
Bone 12 Name: "Bip01 L Forearm"
Bone 13 Name: "Bip01 L Hand"
Bone 14 Name: "Bip01 L Finger0"
Bone 15 Name: "Bip01 L Finger01"
Bone 16 Name: "Bip01 L Finger1"
Bone 17 Name: "Bip01 L Finger11"
Bone 18 Name: "-- L knuckle"
Bone 19 Name: "-- L Forearm twist"
Bone 20 Name: "-- L wrist"
Bone 21 Name: "-- L Elbow"
Bone 22 Name: "-- L bicep twist"
Bone 23 Name: "-- L shoulder outside"
Bone 24 Name: "-- L Shoulder inside"
Bone 25 Name: "Bip01 R Clavicle"
Bone 26 Name: "Bip01 R UpperArm"
Bone 27 Name: "Bip01 R Forearm"
Bone 28 Name: "Bip01 R Hand"
Bone 29 Name: "Bip01 R Finger0"
Bone 30 Name: "Bip01 R Finger01"
Bone 31 Name: "Bip01 R Finger1"
Bone 32 Name: "Bip01 R Finger11"
Bone 33 Name: "-- R knuckle"
Bone 34 Name: "-- R wrist"
Bone 35 Name: "-- R forearm twist"
Bone 36 Name: "-- R Elbow"
Bone 37 Name: "-- R bicep twist"
Bone 38 Name: "-- R Shoulder inside"
Bone 39 Name: "-- R shoulder outside"
Bone 40 Name: "-- Neck smooth"
Bone 41 Name: "-- R Butt"
Bone 42 Name: "-- L butt"
Bone 43 Name: "Bip01 L Thigh"
Bone 44 Name: "Bip01 L Calf"
Bone 45 Name: "Bip01 L Foot"
Bone 46 Name: "Bip01 L Toe0"
Bone 47 Name: "-- L ankle"
Bone 48 Name: "-- L Knee"
Bone 49 Name: "Bip01 R Thigh"
Bone 50 Name: "Bip01 R Calf"
Bone 51 Name: "Bip01 R Foot"
Bone 52 Name: "Bip01 R Toe0"
Bone 53 Name: "-- R Ankle"
Bone 54 Name: "-- R Knee"
Bone 55 Name: "Bomb"

```

#### Usage
```
// ENTITY is the player entity id
// BONE_NUMBER you have to choose from the list above
// bone_origin[3] is the vector where we save the bone origin
// bone_angles[3] the vector that holds the angles of the bone.
engfunc(EngFunc_GetBonePosition, ENTITY, BONE_NUMBER, Float:bone_origin[3], Float:bone_angles[3])
```

#### Useful Stocks
These stocks are made for CS/CZ, you need to port them to other mods. 
##### get_bone_hitgroup
This gets the hitgroup of the bone: 
```
#define BONE_HIT_HEAD		8
#define BONE_HIT_CHEST		6
#define BONE_HIT_STOMACH	4
#define BONE_HIT_LEFTARM	24
#define BONE_HIT_RIGHTARM	39
#define BONE_HIT_LEFTLEG	48
#define BONE_HIT_RIGHTLEG	54
#define HEAD_NECK		40
#define BONE_L_BUTT		41
#define BONE_R_BUTT		42
 
stock get_bone_hitgroup(number)
{
    switch (number)
    {
        case HEAD_NECK:
        {
            return HIT_HEAD
        }
        case BONE_L_BUTT:
        {
            return HIT_LEFTLEG
        }
        case BONE_R_BUTT:
        {
            return HIT_RIGHTLEG
        }
    }
 
    if (1 <= number <= BONE_HIT_STOMACH)
        return HIT_STOMACH
 
    if (BONE_HIT_STOMACH < number <= BONE_HIT_CHEST)
        return HIT_CHEST
 
    if (BONE_HIT_CHEST < number <= BONE_HIT_HEAD)
        return HIT_HEAD
 
    if (BONE_HIT_HEAD < number <= BONE_HIT_LEFTARM)
        return HIT_LEFTARM
 
    if (BONE_HIT_LEFTARM < number <= BONE_HIT_RIGHTARM)
        return HIT_RIGHTARM
 
    if (BONE_HIT_RIGHTARM < number <= BONE_HIT_LEFTLEG)
        return HIT_LEFTLEG
 
    if (BONE_HIT_LEFTLEG < number <= BONE_HIT_RIGHTLEG)
        return HIT_RIGHTLEG
 
    return HIT_GENERIC
}
```

##### find_closest_bone_to_gunshot
This gets the closest bone to the gunshot (Use this in FM_TraceLine and Ham_TraceAttack): 
```
#define DISTANCE_CLEAR_HIT        2.0
 
stock find_closest_bone_to_gunshot(victim, Float:endtrace[3])
{
    new Float:angles[3], Float:origin[3], Float:dist = 9999999.99, Float:curorigin[3], bone_nr
    for (new i=1;i<=54;i++)
    {
        // Get the bone position
        engfunc(EngFunc_GetBonePosition, victim, i, curorigin, angles)
        // Calculate the distance vector
        xs_vec_sub(curorigin, endtrace, angles)
 
        // If this is smaller than the last small distance remember the value!
        if (xs_vec_len(angles) <= dist)
        {
            origin = curorigin
            dist = xs_vec_len(angles)
            bone_nr = i
        }
 
        // If distance is smaller than CLEARHIT! Break (We accept the last value!)
        if (dist <= DISTANCE_CLEAR_HIT)
        {
            break
        }
    }
 
    // Return the bone
    return bone_nr
}
```

## Messaging Functions
### EngFunc_MessageBegin
This function is used to generate client messages. 
#### Usage
Syntax: 
```
engfunc(EngFunc_MessageBegin, dest, msg_type, origin[3] = {0, 0, 0}, player = 0)
```

Example: 
```
static Float:origin[3] // Origin should be a Float
pev(id, pev_origin, origin) // Get user origin
engfunc(EngFunc_MessageBegin,MSG_BROADCAST,SVC_TEMPENTITY,origin,0) // Create message
```

With MSG_ONE_UNRELIABLE: 
```
engfunc(EngFunc_MessageBegin,MSG_ONE_UNRELIABLE,SVC_TEMPENTITY,_,id) // Create message
```

With MSG_ALL: 
```
engfunc(EngFunc_MessageBegin,MSG_ONE_UNRELIABLE,SVC_TEMPENTITY,_,id) // Create message
```

dest can be: 
```
#define    MSG_BROADCAST               0        // Unreliable to all, There is not id
#define    MSG_ONE                     1        // Reliable to one (msg_entity)
#define    MSG_ALL                     2        // Reliable to all, There is not origin
#define    MSG_INIT                    3        // Write to the init string
#define    MSG_PVS                     4        // Ents in PVS of org
#define    MSG_PAS                     5        // Ents in PAS of org
#define    MSG_PVS_R                   6        // Reliable to PVS
#define    MSG_PAS_R                   7        // Reliable to PAS
#define    MSG_ONE_UNRELIABLE          8        // Send to one client, but don't put in reliable stream,
                                                // put in unreliable datagram (could be  dropped), there is not origin
#define    MSG_SPEC                    9        // Sends to all spectator proxies

```

**Before calling another EngFunc_MessageBegin you must call message_end().**
## Entity Search Functions
### EngFunc_FindEntityInSphere
Find entities within a radius. **The function returns the next entity id after the start entity.**
[![](https://wiki.alliedmods.net/images/thumb/FindEntityInSphere.png/300px-FindEntityInSphere.png)](https://wiki.alliedmods.net/File:FindEntityInSphere.png)
[](https://wiki.alliedmods.net/File:FindEntityInSphere.png "Enlarge")
3D diagram to show how the function works.
If we use 
```
engfunc(EngFunc_FindEntityInSphere, -1, origin, radius)
```

In the situation described on the picture the function call above will return 1, 
```
engfunc(EngFunc_FindEntityInSphere, 20, origin, radius)
```

will return 30 and 
```
engfunc(EngFunc_FindEntityInSphere, 100, origin, radius)
```

will return 0, meaning that it didn't find an entity with an id grater than 100. 
#### Usage
```
engfunc(EngFunc_FindEntityInSphere, ent_to_start, origin, radius)
```

### EngFunc_EntitiesInPVS
This function checks entities that are in the [PVS](https://wiki.alliedmods.net/index.php?title=PVS&action=edit&redlink=1 "PVS \(page does not exist\)") of an entity. **It can't be used on worldspawn.**
The function returns the first entity on the [PVS](https://wiki.alliedmods.net/index.php?title=PVS&action=edit&redlink=1 "PVS \(page does not exist\)") and then you can traverse through the results using pev_chain/EV_ENT_chain. A NULL value of pev_chain/EV_ENT_chain indicates the end of the chain. 
#### Usage
```
public whatisonPVS(id)
{
    static next, chain
    static class[32]
 
    next = engfunc(EngFunc_EntitiesInPVS, id)
    while(next)
    {
        pev(next, pev_classname, class, charsmax(class))
        chain = pev(next, pev_chain)
 
        server_print("Found entity in player (%i) PVS: ent(%i) class(%s)", id, next, class)
 
        if(!chain)
            break
 
        next = chain
    }
}
```

### EngFunc_FindEntityByString
Returns the first entity found that matches the search criteria. 
You can use any of string type attributes of entities: 
```
classname	Type of entity
globalname	This is the name of the global variable that can be used to control the state of the entity
model	 	The model of the entity
target	 	Entity that this entity is handling
targetname	The name given to this entity that another entity searches for to handle it
netname		Player or NPC name
message		Seems to be used mainly to store sound (string). It happens to store others things, depending the need of the entity
noise		Noise variables do different things for different ents
noise1		This is the move sound for doors
noise2		This is the stop sound for doors
noise3		This is for blocking game_player_equip and player_weaponstrip

```

#### Usage
```
iEnt = engfunc(EngFunc_FindEntityByString, iStartEnt, sAttribute, sValue)
```

Parameters: 
  * iStartEnt: Start searching on this entity (ex: 0 = worldspawn)
  * sAttribute: Name of attribute over which we need to search (ex: classname)
  * sValue: Text string that we are searching for (ex: func_breakable)


The function returns the first entity matching the criteria. 
### EngFunc_FindClientInPVS
Returns the next "player" entity in someone's [PVS](https://wiki.alliedmods.net/index.php?title=PVS&action=edit&redlink=1 "PVS \(page does not exist\)") using a global loop. 
#### Usage
```
iEnt2 = engfunc(EngFunc_FindClientInPVS, iEnt)
```

Parameters: 
  * iEnt Source entity. Seek someone within iEnt's [PVS](https://wiki.alliedmods.net/index.php?title=PVS&action=edit&redlink=1 "PVS \(page does not exist\)")


Unlike [EntitiesInPVS](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_EntitiesInPVS), it does not return a series of chained entities. Instead, it works like a global loop of entities. No matter which source entity you use, this function maintains the last index used and returns the next entity in source entity [PVS](https://wiki.alliedmods.net/index.php?title=PVS&action=edit&redlink=1 "PVS \(page does not exist\)"). 
This function must be called several times to find every entity in [PVS](https://wiki.alliedmods.net/index.php?title=PVS&action=edit&redlink=1 "PVS \(page does not exist\)") and can also return the source entity but it can't be called twice inside the same function because it will return the same entity. 
#### Notes
It's not clear the main purpose of this function because you can get similar results with [EntitiesInPVS](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_EntitiesInPVS). 
[CheckVisibility](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_CheckVisibility) and [EntitiesInPVS](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_EntitiesInPVS) are better functions to use. 
## Trace Functions
### EngFunc_TraceLine
This function traces between 2 origins and gives us information about it. 
These are the constants we can use as flags: 
```
#define DONT_IGNORE_MONSTERS            0
#define IGNORE_MONSTERS                 1
#define IGNORE_MISSILE                  2
#define IGNORE_GLASS                    0x100

```

**These constants can be used together.**
Ex: IGNORE_MISSILE | IGNORE_MONSTERS | IGNORE_GLASS - This makes the traceline ignore missiles, monsters (players) and glass. 
#### Usage
Example of doing a traceline between two origins, and ignoring glass: 
```
engfunc(EngFunc_TraceLine, start, end, IGNORE_GLASS, 0, tr)
```

Now considering glass: 
```
engfunc(EngFunc_TraceLine, start, end, DONT_IGNORE_MONSTERS, 0, tr)
```

  * [![](https://wiki.alliedmods.net/images/thumb/Traceline1.jpg/120px-Traceline1.jpg)](https://wiki.alliedmods.net/File:Traceline1.jpg)
Traceline result if glass is ignored. The entity is ignored because of its solid flag 
  * [![](https://wiki.alliedmods.net/images/thumb/Traceline2.jpg/120px-Traceline2.jpg)](https://wiki.alliedmods.net/File:Traceline2.jpg)
Traceline result if glass is not ignored. 
  * [![](https://wiki.alliedmods.net/images/thumb/Traceline3.jpg/120px-Traceline3.jpg)](https://wiki.alliedmods.net/File:Traceline3.jpg)
Traceline result if glass is ignored but there's an entity with blocking solid flags in the way 
  * [![](https://wiki.alliedmods.net/images/thumb/Traceline4.jpg/120px-Traceline4.jpg)](https://wiki.alliedmods.net/File:Traceline4.jpg)
Traceline result if glass is ignored, and the entity in the way has non-blocking flags 


#### Other Traceline functions
This creates a trace handle. It's important to do this because we don't want our plugins to mess with eachothers info. 
```
new ptr = create_tr2()
```

And this frees the trace handle: 
```
free_tr2(ptr)
```

Getter and setter: 
```
[g|s]et_tr2(trace_handle, CONSTANT, argument_if_setting)
```

Where CONSTANT can be one of the following enumerations: 
```
enum TraceResult
{
	TR_AllSolid,		// int
	TR_StartSolid,		// int
	TR_InOpen,		// int
	TR_InWater,		// int
	TR_flFraction,		// float
	TR_vecEndPos,		// float array[3]
	TR_flPlaneDist,		// float
	TR_vecPlaneNormal,	// float array[3]
	TR_pHit,		// int (edict_t*)
	TR_iHitgroup,		// int
};
```

**Getting the array and Float values require the third parameter to be passed.**
Example: 
```
    new startsolid = get_tr2(trace, TR_StartSolid)
    // TR_StartSolid is a boolean that says whether you were "inside" something 
    // (usually the world) when the trace started (point A)
    // TR_AllSolid tells you if you ever got out of the "inside" or not.
 
    new inopen = get_tr2(trace, TR_InOpen)
    // TR_InOpen means that the start point is in Open
    // That means in the world and not in an ent or something
 
    new hit = get_tr2(trace, TR_pHit)
    // What was hit by the traceline. It will either be a player index,
    // entity index, 0 (part of map), or -1 (didn't hit anything; 
    // doesn't happen with player tracelines).
 
    new hitgroup = get_tr2(trace, TR_iHitgroup)
    // If the traceline hit another player, returns will be HIT_HEAD,
    // HIT_CHEST, HIT_LEFTLEG... etc. If the traceline hit part of the
    // map, this returns HIT_GENERIC.
 
    new Float:fraction
    get_tr2(trace, TR_flFraction, fraction)
    // Returns a number between 0.0 and 1.0, indicating how far the
    // traceline traveled start to end before it hit something. Depending
    // on what conditions were passed to this traceline forward function,
    // it could either be a wall or another entity.
 
    new Float:end_origin[3]
    get_tr2(trace, TR_vecEndPos, end_origin)
    // The official end of the traceline. Not necesarily the same as the
    // second argument passed to this traceline forward function.
 
    new Float:normal[3]
    get_tr2(trace, TR_vecPlaneNormal, normal)
    // Returns a 1 unit long vector normal to the spot that it hit. Note
    // that "normal" has a special connotation here. It doesn't mean "regular."
```

#### Useful Stocks
##### is_wall_between_points
This returns true if there's a wall between _start_ and _end_. 
```
stock is_wall_between_points(Float:start[3], Float:end[3], ignore_ent)
{
    // Create the trace handle! It is best to create it!
    new ptr = create_tr2()
 
    // The main traceline function!
    // This function ignores GLASS, MISSILE and MONSTERS!
    // Here is an example of how you should combine all the flags!
    engfunc(EngFunc_TraceLine, start, end, IGNORE_GLASS | IGNORE_MONSTERS | IGNORE_MISSILE, ignore_ent, ptr)
 
    // We are interested in the fraction parameter
    new Float: fraction
    get_tr2(ptr, TR_flFraction, fraction)
 
    // Free the trace handle (don't forget to do this!)
    free_tr2(ptr)
 
    // If = 1.0 then it didn't hit anything!
    return (fraction != 1.0)
}
```

#### Extra Info
[[Description of tracelines on the Valve Developer Community](http://developer.valvesoftware.com/wiki/TraceLines)] 
[[Traceline tutorial by Nomexous](http://forums.alliedmods.net/showthread.php?t=66076)] 
### EngFunc_TraceTexture, DLLFunc_PM_FindTextureType
The TraceTexture function detects the texture of an entity from a direction 
The FindTextureType function allows to get the type of the material of the texture. 
#### Usage
```
engfunc(EngFunc_TraceTexture, ent, Float:start[3], Float:end[3], texture_name, len)
```

  * ent is the entity that we want to get the texture
  * start is the point from where the trace starts
  * end is the point where the trace ends
  * texture_name - here we save the texture name
  * len - the texture_name string length


  

```
dllfunc(DLLFunc_PM_FindTextureType, texture_name)
```

  * texture_name is the name of the texture that we have gotten with TraceTexture


The function returns the material of the texture, which can be one of the following: 
  * C : concrete
  * D : dirt
  * G : grate
  * M : metal
  * N : snow
  * P : computer
  * S : slosh
  * T : tile
  * V : ventilation
  * W : wood
  * Y : glass


  

**Example:**
```
new texture_name[64], texture_type
    engfunc(EngFunc_TraceTexture, 0, start, end, texture_name, charsmax(texture_name))
    texture_type = dllfunc(DLLFunc_PM_FindTextureType, texture_name)
```

#### Notes
**Improper use of these functions may crash the server!**
To avoid crashing the server use the TraceTexture: 
  * on any entities (even worldspawn) except players
  * when there is at least one player connected
  * with a big distance between the two points (> 2000.0)


  

### EngFunc_TraceModel
This function traces between 2 origins a model and gives us properties about it. It acts just like a TraceLine but it ignores all the entities except the one we want to hit! 
#### Usage
```
engfunc(EngFunc_TraceModel, const Float:start[3], const Float:end[3], hull, ent_to_hit, ptr)
```

  * start - start origin
  * end - end origin
  * hull - the hull that is moved check above to see them
  * ent_to_hit - the entity that you want to hit (this is a must!)
  * ptr - the trace handle pointer, acts the same as the one in trace line!


The constants that we can use in hull: 
```
#define HULL_POINT                      0  // This means that we are moving a point from the start to the end
#define HULL_HUMAN                      1  // That means that we move a cube of a player from start to end
#define HULL_LARGE                      2  // That means that we move a bigger cube that one of the player from start to end
                                           // (used in HL for big monsters!)
#define HULL_HEAD                       3  // This means that we move from start to end the hull of a ducked player

```

#### Extra Info
[[TraceModel example](http://forums.alliedmods.net/showthread.php?p=850698)] 
[TraceLine explanation](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_TraceLine)
### EngFunc_TraceToss
Trace the point where some entity movement will finish. If for some reason the entity movement must be blocked for other entity (or worldspawn), TraceToss will detect that situation taking in account the original entity bounding boxes. 
#### Usage
```
engfunc(EngFunc_TraceToss, ent, skipent, tr)
```

  * ent = The entity which movement we want to trace
  * skipent = The entity to skip in trace
  * tr = trace handle to store the result


[![](https://wiki.alliedmods.net/images/thumb/Tracetoss.jpg/300px-Tracetoss.jpg)](https://wiki.alliedmods.net/File:Tracetoss.jpg)
[](https://wiki.alliedmods.net/File:Tracetoss.jpg "Enlarge")
EngFunc_TraceToss example
#### Example
In the image you can see a player jumping and 2 points. 
_Start Point_ is the origin of the player when TraceToss was called. 
_End Point_ is the point returned in TR result. 
So the player is making a parabola from START to END. The green line is only for testing purposes and show from where to where the trace is. This was tested with gravity = 400. 
## Model/Decal/Texture Functions
### EngFunc_SetModel
Properly sets a new model on an entity. 
#### Usage
```
engfunc(EngFunc_SetModel, iEnt, sModel)
```

  * iEnt = Entity index
  * sModel = Model file name to set on entity (ex: "models/player/vip/vip.mdl")


#### Engine Alternative
```
entity_set_model(entity, model[])
```

[[FuncWiki page for entity_set_model](http://www.amxmodx.org/funcwiki.php?go=func&id=354)] 
### EngFunc_ModelIndex
Returns an unique index of the model name provided. It's actually the same number that precache_model() returns. 
A model index is used for example in some TE_* messages. ( TE_LIGHTNING, TE_GLOWSPRITE, etc.. See message_const.inc file ). 
The model index of an entity is stored in pev_modelindex. 
#### Usage
```
ModelIndex = engfunc(EngFunc_ModelIndex, "models/MyModel.mdl")
```

ModelIndex will have the model index for "models/MyModel.mdl" after the function call. 
### EngFunc_ModelFrames
Returns the frames count of a model. 
#### Usage
```
ModelFrames = engfunc(EngFunc_ModelFrames, ModelIndex)
```

  * ModelIndex = The model index. Value you can get from precache_model() or [EngFunc_ModelIndex](https://wiki.alliedmods.net/FakeMeta_Functions_Detailed_Descriptions#EngFunc_ModelIndex).


  

### EngFunc_DecalIndex
Returns an unique index of the decal name provided. 
A decal index is used for example in some TE_* messages. ( TE_PLAYERDECAL, TE_DECAL, etc.. See message_const.inc file ). 
All the available decals are stored in the decals.wad file. ( Located at your mod root directory ) 
As side-note a plugin [["Decals/Models Lister"](http://forums.alliedmods.net/showthread.php?p=247677)] is available to see a list of decals/models index/name. ( Only CS and HL ) 
#### Usage
```
DecalIndex = engfunc(EngFunc_DecalIndex, "{bigshot1")
```

DecalIndex will have the decal index for "{bigshot1" after the function call. 
#### Engine alternative
```
DecalIndex = get_decal_index( "{bigshot1" )
```

[[FuncWiki page for get_decal_index()](http://www.amxmodx.org/funcwiki.php?go=func&id=329)] 
### EngFunc_AnimationAutomove
Plays the selected animation on entity 
#### Usage
```
entity_set_float(iEnt, EV_FL_framerate, fFrameRate);
entity_set_int(iEnt, EV_INT_sequence, iSequence);
engfunc(EngFunc_AnimationAutomove, iEnt, fTime);
```

  * fFrameRate = Frame rate of desired animation.
  * iSequence = Sequence to play.
  * iEnt = Source entity.
  * fTime = **It seems to not affect the animation. Maybe for internal use.**


First you have to select the sequence and the desired frame rate. Then you can start the animation. It will run in an endless loop. 
It seems to work only on non-player entities. 
## Entity/Global Functions
### EngFunc_NumberOfEntities
Returns the number of entities in the world. 
#### Usage
```
ents = engfunc(EngFunc_NumberOfEntities)
```

#### Engine alternative
```
ents = entity_count()
```

[[FuncWiki page for entity_count](http://www.amxmodx.org/funcwiki.php?go=func&id=356)] 
### EngFunc_SetSize
Sets the bounds of an entity. 
#### Usage
```
engfunc(EngFunc_SetSize, iEnt, Float:fMins[3], Float:fMaxs[3])
```

  * iEnt = Entity index
  * fMins[3] = Mins boundings values (x,y,z)
  * fMaxs[3] = Maxs boundings values (x,y,z)


#### Engine alternative
```
entity_set_size(index, Float:mins[3], Float:maxs[3])
```

[[FuncWiki page for entity_set_size](http://www.amxmodx.org/funcwiki.php?go=func&id=328)] 
### EngFunc_SetOrigin
Properly sets a new origin on an entity. 
#### Usage
```
engfunc(EngFunc_SetOrigin, iEnt, Float:Origin[3])
```

  * iEnt = Entity index
  * Origin[3] = New origin for the entity (x,y,z)


#### Engine alternative
```
entity_set_origin(index, Float:NewOrigin[3])
```

[[FuncWiki page for entity_set_origin](http://www.amxmodx.org/funcwiki.php?go=func&id=353)] 
### EngFunc_MoveToOrigin
Moves an entity a defined distance toward a coordinate. 
If the distance between Entity and Destination is less than the required distance, the entity will pass over that point. 
#### Usage
```
engfunc(EngFunc_MoveToOrigin, iEnt, Float:Destination[3], Float:Distance, iMoveType)
```

  * iEnt = Entity index
  * Destination[3] = A Coordinate toward which the entity moves
  * Distance = The distance to move the entity
  * iMoveType = This is the MOVE_* option used for monsters and players to change the behaviour of the movement


Move type possible values: 
```
#define MOVE_NORMAL		0	// normal move in the direction monster is facing
#define MOVE_STRAFE		1	// moves in direction specified, no matter which way monster is facing
#define MOVE_STUCK_DIST		32	// if a monster can't step this far, it is stuck.
#define MOVE_START_TURN_DIST	64	// when this far away from moveGoal, start turning to face next goal

```

#### Caveats
  * iEnt must be on ground
  * If there's an object closer than Distance that iEnt could collide then the movement is not done
  * If there's a ramp, it works like an object and the movement is not done


## Visibility Functions
### EngFunc_CheckVisibility
This function is used to check if an entity is in your [PVS](https://wiki.alliedmods.net/index.php?title=PVS&action=edit&redlink=1 "PVS \(page does not exist\)"). 
**It can be used on all entities except worldspawn.**
#### Usage
This function has a parameter that must be obtained in a special way, the _pset_ parameter. **Note:** The parameter is player only, that means that if you get pset for example for a player that has the id _1_. When you use this function on an entity it will check whether that entity is in [PVS](https://wiki.alliedmods.net/index.php?title=PVS&action=edit&redlink=1 "PVS \(page does not exist\)") of the Player id _1_. 
```
new g_cl_pset[33]
 
public plugin_init(id)
{
    register_forward(FM_AddToFullPack, "pfw_atfp", 1)
}
 
public pfw_atfp(es, e, ent, host, flags, player, set)
{
    g_cl_pset[host] = set
 
    return FMRES_IGNORED
}
 
stock is_ent_in_player_pvs(id, entity)
{
    return engfunc(EngFunc_CheckVisibility, entity, g_cl_pset[id])
}
 
stock get_pvs_players(id, players[32], num, flags[], team[])
{
    if (!is_user_connected(id))
        return 0    
 
    get_players(players, num, flags, team)
 
    for (new i=0;i<num;i++)
    {
        if (!is_ent_in_player_pvs(id, players[i]))
        {
            num--;
 
            for (new j=i;j<num;j++)
            {
                players[j] = players[j+1]
            }
 
            i--
        }
    }
 
    return 1
}
```

## Other Functions
### EngFunc_PrecacheModel
Precaches a model or sprite file. 
This should be used only when you would need to postpone the precache process in plugin_init() or plugin_cfg(), otherwise you should use precache_model() native directly in plugin_precache() forward. 
It can be useful for example when you want to manage models with cvars and to avoid registering them in plugin_precache() then getting some trouble, you could manage out of this forward. 
#### Usage
```
engfunc(EngFunc_PrecacheModel, "models/MyModel.mdl")
```
```
engfunc(EngFunc_PrecacheModel, "sprites/MySprite.spr")
```

It returns the precached model/sprite index if successful, otherwise 0. 
### EngFunc_PrecacheSound
Precaches a sound, only *.wav file. ( for mp3, see EngFunc_PrecacheGeneric ) 
This should be used only when you would need to postpone the precache process in plugin_init() or plugin_cfg(), otherwise you should use precache_sound() native directly in plugin_precache() forward. 
It can be useful for example when you want to manage sounds with cvars and to avoid registering them in plugin_precache() then getting some trouble, you could manage out of this forward. 
#### Usage
```
engfunc(EngFunc_PrecacheSound, "sound/MySound.wav")
```

It returns the precached sound index if successful, otherwise 0. 
### EngFunc_AlertMessage
Prints an alert message. 
#### Usage
```
engfunc(EngFunc_AlertMessage, AlertType, const Message)
```

AlertType can be: 
```
at_notice - shows a message box with the message
at_console - same as at_notice, but forces a ConPrintf, not a message box, prints output to server console, but only if 'developer' is 1.
at_aiconsole - same as at_console, but only shown if 'developer' is 2.
at_warning -
at_error -
at_logged - prints output to server logs and console.

```

