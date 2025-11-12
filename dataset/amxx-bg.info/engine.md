# Functions in engine.inc
Function | Description  
---|---  
[traceresult](https://amxx-bg.info/api/engine/traceresult) | ```
Retrieves a result from the global engine module trace handle.
```
  
[register_impulse](https://amxx-bg.info/api/engine/register_impulse) | ```
Registers a function to be called on a client impulse.
```
  
[register_touch](https://amxx-bg.info/api/engine/register_touch) | ```
Registers a function to be called on a touch action between entities of
specified classes.
```
  
[register_think](https://amxx-bg.info/api/engine/register_think) | ```
Registers a function to be called on entity think on all entities of a
specified class.
```
  
[unregister_impulse](https://amxx-bg.info/api/engine/unregister_impulse) | ```
Removes a previously registered impulse hook.
```
  
[unregister_touch](https://amxx-bg.info/api/engine/unregister_touch) | ```
Removes a previously registered touch hook.
```
  
[unregister_think](https://amxx-bg.info/api/engine/unregister_think) | ```
Removes a previously registered think hook.
```
  
[set_speak](https://amxx-bg.info/api/engine/set_speak) | ```
Sets the engine module speak flags on a client.
```
  
[get_speak](https://amxx-bg.info/api/engine/get_speak) | ```
Returns the engine module speak flags currently set on a client.
```
  
[drop_to_floor](https://amxx-bg.info/api/engine/drop_to_floor) | ```
Uses the DROP_TO_FLOOR() engine function on an entity, which attempts to put
it down on the floor.
```
  
[get_info_keybuffer](https://amxx-bg.info/api/engine/get_info_keybuffer) | ```
Retrieves keyvalue buffer from a client or the server.
```
  
[force_use](https://amxx-bg.info/api/engine/force_use) | ```
Forces an entity (such as a player) to use another entity (such as a button).
```
  
[get_global_float](https://amxx-bg.info/api/engine/get_global_float) | ```
Returns a float type value from the server globals.
```
  
[get_global_int](https://amxx-bg.info/api/engine/get_global_int) | ```
Returns a integer type value from the server globals.
```
  
[get_global_string](https://amxx-bg.info/api/engine/get_global_string) | ```
Retrieves a global string type value from the server.
```
  
[get_global_vector](https://amxx-bg.info/api/engine/get_global_vector) | ```
Returns a vector type value from the server globals.
```
  
[get_global_edict](https://amxx-bg.info/api/engine/get_global_edict) | ```
Returns a edict type value from the server globals.
```
  
[get_global_edict2](https://amxx-bg.info/api/engine/get_global_edict2) | ```
Returns a edict type value from the server globals.
```
  
[entity_set_size](https://amxx-bg.info/api/engine/entity_set_size) | ```
Sets the size of the entity bounding box, as described by the minimum and
maximum vectors relative to the origin.
```
  
[get_decal_index](https://amxx-bg.info/api/engine/get_decal_index) | ```
Returns the index of a decal.
```
  
[entity_range](https://amxx-bg.info/api/engine/entity_range) | ```
Returns the distance between two entities.
```
  
[entity_intersects](https://amxx-bg.info/api/engine/entity_intersects) | ```
Returns if two entities bounding boxes intersect by comparing their absolute
minimum and maximum origins.
```
  
[entity_get_int](https://amxx-bg.info/api/engine/entity_get_int) | ```
Returns an integer type value from an entities entvar struct.
```
  
[entity_set_int](https://amxx-bg.info/api/engine/entity_set_int) | ```
Sets an integer type value in an entities entvar struct.
```
  
[entity_get_float](https://amxx-bg.info/api/engine/entity_get_float) | ```
Returns a float type value from an entities entvar struct.
```
  
[entity_set_float](https://amxx-bg.info/api/engine/entity_set_float) | ```
Sets a float type value in an entities entvar struct.
```
  
[entity_get_vector](https://amxx-bg.info/api/engine/entity_get_vector) | ```
Retrieves a vector type value from an entities entvar struct.
```
  
[entity_set_vector](https://amxx-bg.info/api/engine/entity_set_vector) | ```
Sets a vector type value in an entities entvar struct.
```
  
[entity_get_edict](https://amxx-bg.info/api/engine/entity_get_edict) | ```
Returns an edict type value from an entities entvar struct.
```
  
[entity_get_edict2](https://amxx-bg.info/api/engine/entity_get_edict2) | ```
Returns an edict type value from an entities entvar struct.
```
  
[entity_set_edict](https://amxx-bg.info/api/engine/entity_set_edict) | ```
Sets an edict type value in an entities entvar struct.
```
  
[entity_get_string](https://amxx-bg.info/api/engine/entity_get_string) | ```
Retrieves a string type value from an entities entvar struct.
```
  
[entity_set_string](https://amxx-bg.info/api/engine/entity_set_string) | ```
Sets a string type value in an entities entvar struct.
```
  
[entity_get_byte](https://amxx-bg.info/api/engine/entity_get_byte) | ```
Returns a bytearray type value from an entities entvar struct.
```
  
[entity_set_byte](https://amxx-bg.info/api/engine/entity_set_byte) | ```
Sets a bytearray type value in an entities entvar struct.
```
  
[create_entity](https://amxx-bg.info/api/engine/create_entity) | ```
Creates an entity.
```
  
[remove_entity](https://amxx-bg.info/api/engine/remove_entity) | ```
Removes an entity from the world.
```
  
[entity_count](https://amxx-bg.info/api/engine/entity_count) | ```
Returns the current number of entities in the world.
```
  
[is_valid_ent](https://amxx-bg.info/api/engine/is_valid_ent) | ```
Returns if an entity index is valid (as required by other engine natives).
```
  
[find_ent_by_class](https://amxx-bg.info/api/engine/find_ent_by_class) | ```
Searches entities in the world, starting at a specified index and matching by
classname.
```
  
[find_ent_by_owner](https://amxx-bg.info/api/engine/find_ent_by_owner) | ```
Searches entities in the world, starting at a specified index, matching by
owner and a configurable entity field.
```
  
[find_ent_by_target](https://amxx-bg.info/api/engine/find_ent_by_target) | ```
Searches entities in the world, starting at a specified index and matching by
target.
```
  
[find_ent_by_tname](https://amxx-bg.info/api/engine/find_ent_by_tname) | ```
Searches entities in the world, starting at a specified index and matching by
targetname.
```
  
[find_ent_by_model](https://amxx-bg.info/api/engine/find_ent_by_model) | ```
Searches entities in the world, starting at a specified index and matching by
classname and model.
```
  
[find_ent_in_sphere](https://amxx-bg.info/api/engine/find_ent_in_sphere) | ```
Searches for entities inside a sphere, starting at a specified index.
```
  
[find_sphere_class](https://amxx-bg.info/api/engine/find_sphere_class) | ```
Searches for entities inside a sphere around a specified entity or origin,
matching by classname.
```
  
[entity_set_origin](https://amxx-bg.info/api/engine/entity_set_origin) | ```
Sets the origin of an entity.
```
  
[entity_set_model](https://amxx-bg.info/api/engine/entity_set_model) | ```
Sets the model of an entity.
```
  
[set_ent_rendering](https://amxx-bg.info/api/engine/set_ent_rendering) | ```
Sets rendering options of an entity.
```
  
[call_think](https://amxx-bg.info/api/engine/call_think) | ```
Calls the DispatchThink() game DLL function on an entity, triggering it to
think if applicable.
```
  
[fake_touch](https://amxx-bg.info/api/engine/fake_touch) | ```
Forces an entity to touch another entity.
```
  
[DispatchSpawn](https://amxx-bg.info/api/engine/DispatchSpawn) | ```
Calls the spawn function on an entity.
```
  
[DispatchKeyValue](https://amxx-bg.info/api/engine/DispatchKeyValue) | ```
Fires/sets a keyvalue on an entity.
```
  
[get_keyvalue](https://amxx-bg.info/api/engine/get_keyvalue) | ```
Retrieves a value from an entities keyvalues.
```
  
[copy_keyvalue](https://amxx-bg.info/api/engine/copy_keyvalue) | ```
Retrieves buffers from the keyvalue structure.
```
  
[radius_damage](https://amxx-bg.info/api/engine/radius_damage) | ```
Hurts (and kills, if applicable) players in a sphere.
```
  
[point_contents](https://amxx-bg.info/api/engine/point_contents) | ```
Returns the contents value of an origin.
```
  
[is_in_viewcone](https://amxx-bg.info/api/engine/is_in_viewcone) | ```
Returns if an origin is in an entities view cone. Derived from SDK.
```
  
[is_visible](https://amxx-bg.info/api/engine/is_visible) | ```
Returns if an entity is visible to another entity. Derived from SDK.
```
  
[trace_line](https://amxx-bg.info/api/engine/trace_line) | ```
Fires a trace line between two origins, retrieving the end point and entity
hit.
```
  
[trace_normal](https://amxx-bg.info/api/engine/trace_normal) | ```
Fires a trace line between two origins, retrieving the trace normal.
```
  
[trace_hull](https://amxx-bg.info/api/engine/trace_hull) | ```
Fires a trace hull on a specified origin or between two origins.
```
  
[trace_forward](https://amxx-bg.info/api/engine/trace_forward) | ```
Attempts to describe an obstacle by firing trace lines in a specified
direction, offset on the z-axis around an origin.
```
  
[get_grenade_id](https://amxx-bg.info/api/engine/get_grenade_id) | ```
Finds a grenade entity, matching by owner.
```
  
[halflife_time](https://amxx-bg.info/api/engine/halflife_time) | ```
Returns the game time based on the game tick.
```
  
[set_lights](https://amxx-bg.info/api/engine/set_lights) | ```
Sets the map lighting level.
```
  
[attach_view](https://amxx-bg.info/api/engine/attach_view) | ```
Attaches a clients viewport to an entity.
```
  
[set_view](https://amxx-bg.info/api/engine/set_view) | ```
Sets the engine module view mode on a client.
```
  
[playback_event](https://amxx-bg.info/api/engine/playback_event) | ```
Plays back an event on the client. Most prominently used for gun firing
animations.
```
  
[get_usercmd](https://amxx-bg.info/api/engine/get_usercmd) | ```
Retrieves a value from a usercmd struct.
```
  
[set_usercmd](https://amxx-bg.info/api/engine/set_usercmd) | ```
Sets a value in a usercmd struct.
```
  
[eng_get_string](https://amxx-bg.info/api/engine/eng_get_string) | ```
Retrieves a string from the engine string table.
```
  
[pfn_touch](https://amxx-bg.info/api/engine/pfn_touch) | ```
Called when two entities touch.
```
  
[server_frame](https://amxx-bg.info/api/engine/server_frame) | ```
Called at the start of every server frame.
```
  
[client_kill](https://amxx-bg.info/api/engine/client_kill) | ```
Called when a client types kill in console.
```
  
[client_PreThink](https://amxx-bg.info/api/engine/client_PreThink) | ```
Called at the start of each client think.
```
  
[client_PostThink](https://amxx-bg.info/api/engine/client_PostThink) | ```
Called after each client think.
```
  
[client_impulse](https://amxx-bg.info/api/engine/client_impulse) | ```
Called when a client triggers an impulse.
```
  
[client_cmdStart](https://amxx-bg.info/api/engine/client_cmdStart) | ```
Called for CmdStart() on a client.
```
  
[pfn_think](https://amxx-bg.info/api/engine/pfn_think) | ```
Called when an entity thinks.
```
  
[pfn_playbackevent](https://amxx-bg.info/api/engine/pfn_playbackevent) | ```
Called when an event is played.
```
  
[pfn_keyvalue](https://amxx-bg.info/api/engine/pfn_keyvalue) | ```
Called when a keyvalue pair is sent to an entity.
```
  
[pfn_spawn](https://amxx-bg.info/api/engine/pfn_spawn) | ```
Called when an entity is spawned.
```
  

This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

