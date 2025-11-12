# Functions in reapi_engine.inc
Function | Description  
---|---  
[set_entvar](https://amxx-bg.info/api/reapi_engine/set_entvar) | ```
Sets entvars data for an entity.
Use the var_* EntVars enum
```
  
[get_entvar](https://amxx-bg.info/api/reapi_engine/get_entvar) | ```
Returns entvar data from an entity.
Use the var_* EntVars enum
```
  
[set_ucmd](https://amxx-bg.info/api/reapi_engine/set_ucmd) | ```
Sets usercmd data.
Use the ucmd_* UCmd enum
```
  
[get_ucmd](https://amxx-bg.info/api/reapi_engine/get_ucmd) | ```
Returns usercmd data from an entity.
Use the ucmd_* UCmd enum
```
  
[get_key_value](https://amxx-bg.info/api/reapi_engine/get_key_value) | ```
Gets value for key in buffer
```
  
[set_key_value](https://amxx-bg.info/api/reapi_engine/set_key_value) | ```
Sets value for key in buffer
```
  
[GetBonePosition](https://amxx-bg.info/api/reapi_engine/GetBonePosition) | ```
Gets the position of the bone
```
  
[GetAttachment](https://amxx-bg.info/api/reapi_engine/GetAttachment) | ```
Gets the position of the attachment
```
  
[rh_set_mapname](https://amxx-bg.info/api/reapi_engine/rh_set_mapname) | ```
Sets the name of the map.
```
  
[rh_get_mapname](https://amxx-bg.info/api/reapi_engine/rh_get_mapname) | ```
Gets the name of the map.
```
  
[rh_reset_mapname](https://amxx-bg.info/api/reapi_engine/rh_reset_mapname) | ```
Reverts back the original map name.
```
  
[rh_emit_sound2](https://amxx-bg.info/api/reapi_engine/rh_emit_sound2) | ```
Emits a sound from an entity from the engine.
```
  
[rh_update_user_info](https://amxx-bg.info/api/reapi_engine/rh_update_user_info) | ```
Forces an userinfo update
```
  
[rh_drop_client](https://amxx-bg.info/api/reapi_engine/rh_drop_client) | ```
Kicks a client from server with message
```
  
[rh_get_net_from](https://amxx-bg.info/api/reapi_engine/rh_get_net_from) | ```
-
```
  
[set_netadr](https://amxx-bg.info/api/reapi_engine/set_netadr) | ```
Sets a NetAdr var.
```
  
[get_netadr](https://amxx-bg.info/api/reapi_engine/get_netadr) | ```
Returns a NetAdr var
```
  
[get_key_value_buffer](https://amxx-bg.info/api/reapi_engine/get_key_value_buffer) | ```
Gets an AMXX string buffer from a infobuffer pointer
```
  
[set_key_value_buffer](https://amxx-bg.info/api/reapi_engine/set_key_value_buffer) | ```
Sets value string to entire buffer
```
  
[SetBodygroup](https://amxx-bg.info/api/reapi_engine/SetBodygroup) | ```
Sets body group value based on entity's model group
```
  
[GetBodygroup](https://amxx-bg.info/api/reapi_engine/GetBodygroup) | ```
Gets body group value based on entity's model group
```
  
[GetSequenceInfo](https://amxx-bg.info/api/reapi_engine/GetSequenceInfo) | ```
Gets sequence information based on entity's model current sequence index
```
  
[rh_get_client_connect_time](https://amxx-bg.info/api/reapi_engine/rh_get_client_connect_time) | ```
Returns client's netchan playing time in seconds.
```
  
[set_netchan](https://amxx-bg.info/api/reapi_engine/set_netchan) | ```
Sets netchan data.
Use the net_* NetChan enum
```
  
[get_netchan](https://amxx-bg.info/api/reapi_engine/get_netchan) | ```
Returns metchan data from an client.
Use the net_* NetChan enum
```
  
[CheckVisibilityInOrigin](https://amxx-bg.info/api/reapi_engine/CheckVisibilityInOrigin) | ```
Test visibility of an entity from a given origin using either PVS or PAS
```
  
[rh_is_entity_fullpacked](https://amxx-bg.info/api/reapi_engine/rh_is_entity_fullpacked) | ```
Checks if a specific entity is present in the host's outgoing entity table for a given frame,
indicating it has passed the visibility check (AddToFullPack) and is ready for client transmission.
```
  
[rh_get_realtime](https://amxx-bg.info/api/reapi_engine/rh_get_realtime) | ```
Get real game time throughout the entire server lifecycle.
```
  
[RegisterMessage](https://amxx-bg.info/api/reapi_engine/RegisterMessage) | ```
Registers a callback function to be called when a game message with the specified ID is received.
```
  
[UnregisterMessage](https://amxx-bg.info/api/reapi_engine/UnregisterMessage) | ```
Unregisters a game message hook identified by the specified handle.
```
  
[EnableHookMessage](https://amxx-bg.info/api/reapi_engine/EnableHookMessage) | ```
Enables a game message hook identified by the specified handle.
```
  
[DisableHookMessage](https://amxx-bg.info/api/reapi_engine/DisableHookMessage) | ```
Disables a game message hook identified by the specified handle.
```
  
[SetMessageData](https://amxx-bg.info/api/reapi_engine/SetMessageData) | ```
Sets the message data in the current game message.
```
  
[GetMessageData](https://amxx-bg.info/api/reapi_engine/GetMessageData) | ```
Gets the message data value in the current game message
```
  
[GetMessageOrigData](https://amxx-bg.info/api/reapi_engine/GetMessageOrigData) | ```
Gets the message data original value in the current game message.
```
  
[GetMessageArgType](https://amxx-bg.info/api/reapi_engine/GetMessageArgType) | ```
Retrieves the type of the argument at the specified number in the current game message.
```
  
[GetMessageArgsNum](https://amxx-bg.info/api/reapi_engine/GetMessageArgsNum) | ```
Retrieves the number of argument in the current game message.
```
  
[SetMessageBlock](https://amxx-bg.info/api/reapi_engine/SetMessageBlock) | ```
Sets the block type for the specified message ID.
```
  
[GetMessageBlock](https://amxx-bg.info/api/reapi_engine/GetMessageBlock) | ```
Retrieves the block type for the specified message ID.
```
  
[IsMessageDataModified](https://amxx-bg.info/api/reapi_engine/IsMessageDataModified) | ```
Checks if the specified type of message data has been modified

This native allows you to check if any part of the message data, such as its
destination, type, origin, receiver, or any the specific argument of the message, has been modified
```
  
[ResetModifiedMessageData](https://amxx-bg.info/api/reapi_engine/ResetModifiedMessageData) | ```
Resets a specific type of message data to its original value
```
  

This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.