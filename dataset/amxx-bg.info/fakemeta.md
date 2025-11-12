# Functions in fakemeta.inc
Function | Description  
---|---  
[pev](https://amxx-bg.info/api/fakemeta/pev) | ```
Returns entvar data from an entity.  Use the pev_* enum (in fakemeta_const.inc) to specify which data you want retrieved.
```
  
[set_pev](https://amxx-bg.info/api/fakemeta/set_pev) | ```
Sets entvar data for an entity.  Use the pev_* enum from fakemeta_const.inc for reference.
```
  
[set_pev_string](https://amxx-bg.info/api/fakemeta/set_pev_string) | ```
Use this native to set a pev field to a string that is already allocated (via a function such
as EngFunc_AllocString).
```
  
[pev_valid](https://amxx-bg.info/api/fakemeta/pev_valid) | ```
Checks the validity of an entity.
```
  
[pev_serial](https://amxx-bg.info/api/fakemeta/pev_serial) | ```
Returns the serial number for each entity.  The serial number is a unique identity
generated when an entity is created.
```
  
[global_get](https://amxx-bg.info/api/fakemeta/global_get) | ```
Returns any global variable inside globalvars_t structure. Use the glb_* enum.

When returning data from glb_pStringBase (the global string table), you may give a pointer into that table
in order to get different strings.
Example:
new model[128]
new ptr = pev(id, pev_viewmodel)
global_get(glb_pStringBase, ptr, model, 127)
```
  
[get_pdata_int](https://amxx-bg.info/api/fakemeta/get_pdata_int) | ```
Returns a integer from an entity's private data.

_linuxdiff value is what to add to the _Offset for linux servers.
_macdiff value is what to add to the _Offset for os x servers.

A log error is thrown on invalid _index and _Offset.
```
  
[set_pdata_int](https://amxx-bg.info/api/fakemeta/set_pdata_int) | ```
Sets an integer to an entity's private data.

_linuxdiff value is what to add to the _Offset for linux servers.
_macdiff value is what to add to the _Offset for os x servers.

A log error is thrown on invalid _index and _Offset.
```
  
[get_pdata_float](https://amxx-bg.info/api/fakemeta/get_pdata_float) | ```
Returns a float from an entity's private data.

_linuxdiff value is what to add to the _Offset for linux servers.
_macdiff value is what to add to the _Offset for os x servers.

A log error is thrown on invalid _index and _Offset.
```
  
[set_pdata_float](https://amxx-bg.info/api/fakemeta/set_pdata_float) | ```
Sets a float to an entity's private data.

_linuxdiff value is what to add to the _Offset for linux servers.
_macdiff value is what to add to the _Offset for os x servers.

A log error is thrown on invalid _index and _Offset.
```
  
[get_pdata_ent](https://amxx-bg.info/api/fakemeta/get_pdata_ent) | ```
Tries to retrieve an edict pointer from an entity's private data.

This function is byte-addressable.  Unlike get_pdata_int() which searches in byte increments of 4,
get_pdata_ent searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _Offset.
```
  
[set_pdata_ent](https://amxx-bg.info/api/fakemeta/set_pdata_ent) | ```
Sets an edict pointer to an entity's private data.

This function is byte-addressable.  Unlike set_pdata_int() which searches in byte increments of 4,
set_pdata_ent searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[get_pdata_bool](https://amxx-bg.info/api/fakemeta/get_pdata_bool) | ```
Returns a boolean from an entity's private data.

This function is byte-addressable. Unlike get_pdata_int() which searches in byte increments of 4,
get_pdata_bool searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[set_pdata_bool](https://amxx-bg.info/api/fakemeta/set_pdata_bool) | ```
Sets a boolean to an entity's private data.

This function is byte-addressable. Unlike set_pdata_int() which searches in byte increments of 4,
set_pdata_bool searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[get_pdata_byte](https://amxx-bg.info/api/fakemeta/get_pdata_byte) | ```
Returns a byte value from an entity's private data.

This function is byte-addressable. Unlike get_pdata_int() which searches in byte increments of 4,
get_pdata_byte searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[set_pdata_byte](https://amxx-bg.info/api/fakemeta/set_pdata_byte) | ```
Sets a byte value to an entity's private data.

This function is byte-addressable. Unlike set_pdata_int() which searches in byte increments of 4,
set_pdata_byte searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[get_pdata_short](https://amxx-bg.info/api/fakemeta/get_pdata_short) | ```
Returns a short value from an entity's private data.

This function is byte-addressable. Unlike get_pdata_int() which searches in byte increments of 4,
get_pdata_short searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[set_pdata_short](https://amxx-bg.info/api/fakemeta/set_pdata_short) | ```
Sets a short value to an entity's private data.

This function is byte-addressable.  Unlike set_pdata_int() which searches in byte increments of 4,
set_pdata_short searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[get_pdata_vector](https://amxx-bg.info/api/fakemeta/get_pdata_vector) | ```
Returns a vector from an entity's private data.

This function is byte-addressable. Unlike get_pdata_int() which searches in byte increments of 4,
get_pdata_vector searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[set_pdata_vector](https://amxx-bg.info/api/fakemeta/set_pdata_vector) | ```
Sets a vector to an entity's private data.

This function is byte-addressable.  Unlike set_pdata_int() which searches in byte increments of 4,
set_pdata_vector searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _Offset.
```
  
[get_pdata_ehandle](https://amxx-bg.info/api/fakemeta/get_pdata_ehandle) | ```
Tries to retrieve an edict (entity encapsulation) pointer from an entity's private data.

This function is byte-addressable.  Unlike get_pdata_int() which searches in byte increments of 4,
get_pdata_ehandle searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _offset.
```
  
[set_pdata_ehandle](https://amxx-bg.info/api/fakemeta/set_pdata_ehandle) | ```
Sets an edict (entity encapsulation) pointer to an entity's private data.

This function is byte-addressable.  Unlike set_pdata_int() which searches in byte increments of 4,
set_pdata_ehandle searches in increments of 1.

_linuxdiff value is what to add to the _offset for linux servers.
_macdiff value is what to add to the _offset for os x servers.

A log error is thrown on invalid _index and _Offset.
```
  
[register_forward](https://amxx-bg.info/api/fakemeta/register_forward) | ```
Registers a forward.
Returns an id you can pass to unregister_forward
```
  
[unregister_forward](https://amxx-bg.info/api/fakemeta/unregister_forward) | ```
Unregisters a forward.
The registerId must be from register_forward, and
post/forwardtype must match what you registered the forward as.
```
  
[forward_return](https://amxx-bg.info/api/fakemeta/forward_return) | ```
Returns data for metamod
```
  
[get_orig_retval](https://amxx-bg.info/api/fakemeta/get_orig_retval) | ```
Returns the original return value of an engine function.
This is only valid in forwards that were registered as post.

get_orig_retval() - no params, retrieves integer return value
get_orig_retval(&Float:value) - retrieves float return value by reference
get_orig_retval(value[], len) - retrives string return value
```
  
[engfunc](https://amxx-bg.info/api/fakemeta/engfunc) | ```
This function has no description.
```
  
[dllfunc](https://amxx-bg.info/api/fakemeta/dllfunc) | ```
This function has no description.
```
  
[get_tr](https://amxx-bg.info/api/fakemeta/get_tr) | ```
This function has no description.
```
  
[set_tr](https://amxx-bg.info/api/fakemeta/set_tr) | ```
This function has no description.
```
  
[get_tr2](https://amxx-bg.info/api/fakemeta/get_tr2) | ```
This function has no description.
```
  
[set_tr2](https://amxx-bg.info/api/fakemeta/set_tr2) | ```
This function has no description.
```
  
[create_tr2](https://amxx-bg.info/api/fakemeta/create_tr2) | ```
Creates a traceresult handle.  This value should never be altered.
The handle can be used in get/set_tr2 and various traceresult engine functions.

NOTE: You must call free_tr2() on every handle made with create_tr2().
```
  
[free_tr2](https://amxx-bg.info/api/fakemeta/free_tr2) | ```
Frees a traceresult handle created with free_tr2().  Do not call
this more than once per handle, or on handles not created through
create_tr2().
```
  
[get_kvd](https://amxx-bg.info/api/fakemeta/get_kvd) | ```
This function has no description.
```
  
[set_kvd](https://amxx-bg.info/api/fakemeta/set_kvd) | ```
This function has no description.
```
  
[create_kvd](https://amxx-bg.info/api/fakemeta/create_kvd) | ```
Creates a KeyValueData handle.
```
  
[free_kvd](https://amxx-bg.info/api/fakemeta/free_kvd) | ```
Frees a KeyValueData handle.
```
  
[get_cd](https://amxx-bg.info/api/fakemeta/get_cd) | ```
This function has no description.
```
  
[set_cd](https://amxx-bg.info/api/fakemeta/set_cd) | ```
This function has no description.
```
  
[get_es](https://amxx-bg.info/api/fakemeta/get_es) | ```
This function has no description.
```
  
[set_es](https://amxx-bg.info/api/fakemeta/set_es) | ```
This function has no description.
```
  
[get_uc](https://amxx-bg.info/api/fakemeta/get_uc) | ```
This function has no description.
```
  
[set_uc](https://amxx-bg.info/api/fakemeta/set_uc) | ```
This function has no description.
```
  
[get_pdata_string](https://amxx-bg.info/api/fakemeta/get_pdata_string) | ```
This function has no description.
```
  
[set_pdata_string](https://amxx-bg.info/api/fakemeta/set_pdata_string) | ```
This function has no description.
```
  
[copy_infokey_buffer](https://amxx-bg.info/api/fakemeta/copy_infokey_buffer) | ```
This function has no description.
```
  
[lookup_sequence](https://amxx-bg.info/api/fakemeta/lookup_sequence) | ```
Looks up the sequence for the entity.
```
  
[set_controller](https://amxx-bg.info/api/fakemeta/set_controller) | ```
Sets a bone controller with the specified value.
```
  
[get_ent_data](https://amxx-bg.info/api/fakemeta/get_ent_data) | ```
Retrieves an integer value from an entity's private data based off a class
and member name.
```
  
[set_ent_data](https://amxx-bg.info/api/fakemeta/set_ent_data) | ```
Sets an integer value to an entity's private data based off a class
and member name.
```
  
[get_ent_data_float](https://amxx-bg.info/api/fakemeta/get_ent_data_float) | ```
Retrieves a float value from an entity's private data based off a class
and member name.
```
  
[set_ent_data_float](https://amxx-bg.info/api/fakemeta/set_ent_data_float) | ```
Sets a float value to an entity's private data based off a class
and member name.
```
  
[get_ent_data_vector](https://amxx-bg.info/api/fakemeta/get_ent_data_vector) | ```
Retrieves a vector from an entity's private data based off a class and member name.
```
  
[set_ent_data_vector](https://amxx-bg.info/api/fakemeta/set_ent_data_vector) | ```
Sets a vector to an entity's private data based off a class and member name.
```
  
[get_ent_data_entity](https://amxx-bg.info/api/fakemeta/get_ent_data_entity) | ```
Retrieves an entity index from an entity's private data based off a class
and member name.
```
  
[set_ent_data_entity](https://amxx-bg.info/api/fakemeta/set_ent_data_entity) | ```
Sets an entity index to an entity's private data based off a class
and member name.
```
  
[get_ent_data_string](https://amxx-bg.info/api/fakemeta/get_ent_data_string) | ```
Retrieves a string from an entity's private data based off a class and member name.
```
  
[set_ent_data_string](https://amxx-bg.info/api/fakemeta/set_ent_data_string) | ```
Sets a string to an entity's private data based off a class and member name.
```
  
[get_ent_data_size](https://amxx-bg.info/api/fakemeta/get_ent_data_size) | ```
Retrieves the size of array of n entity class member.
```
  
[find_ent_data_info](https://amxx-bg.info/api/fakemeta/find_ent_data_info) | ```
Finds a offset based off an entity class and member name.
```
  
[get_gamerules_int](https://amxx-bg.info/api/fakemeta/get_gamerules_int) | ```
Retrieves an integer value from the gamerules object based off a class
and member name.
```
  
[set_gamerules_int](https://amxx-bg.info/api/fakemeta/set_gamerules_int) | ```
Sets an integer value to the gamerules objecta based off a class
and member name.
```
  
[get_gamerules_float](https://amxx-bg.info/api/fakemeta/get_gamerules_float) | ```
Retrieves a float value from the gamerules object based off a class
and member name.
```
  
[set_gamerules_float](https://amxx-bg.info/api/fakemeta/set_gamerules_float) | ```
Sets a float value to the gamerules object based off a class
and member name.
```
  
[get_gamerules_vector](https://amxx-bg.info/api/fakemeta/get_gamerules_vector) | ```
Retrieves a vector from the gamerules object based off a class and member name.
```
  
[set_gamerules_vector](https://amxx-bg.info/api/fakemeta/set_gamerules_vector) | ```
Sets a vector to the gamerules object based off a class and member name.
```
  
[get_gamerules_entity](https://amxx-bg.info/api/fakemeta/get_gamerules_entity) | ```
Retrieves an entity index from the gamerules object based off a class
and member name.
```
  
[set_gamerules_entity](https://amxx-bg.info/api/fakemeta/set_gamerules_entity) | ```
Sets an entity index to the gamerules object based off a class
and member name.
```
  
[get_gamerules_string](https://amxx-bg.info/api/fakemeta/get_gamerules_string) | ```
Retrieves a string from the gamerules object based off a class and member name.
```
  
[set_gamerules_string](https://amxx-bg.info/api/fakemeta/set_gamerules_string) | ```
Sets a string to the gamerules object based off a class and member name.
```
  
[get_gamerules_size](https://amxx-bg.info/api/fakemeta/get_gamerules_size) | ```
Retrieves the size of array of a gamerules class member.
```
  
[find_gamerules_info](https://amxx-bg.info/api/fakemeta/find_gamerules_info) | ```
Finds a gamerules offset based off a class and member name.
```
  
[get_field_basetype](https://amxx-bg.info/api/fakemeta/get_field_basetype) | ```
Returns the data field base type based off a specific field type.
```
  
[GetModelBoundingBox](https://amxx-bg.info/api/fakemeta/GetModelBoundingBox) | ```
Gets size of a model bounding box.
```
  

This code is a part of fakemeta.inc. To use this code you should include fakemeta.inc as ```#include <fakemeta>```


  
  

