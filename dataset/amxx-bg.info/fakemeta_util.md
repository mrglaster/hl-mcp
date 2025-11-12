# Functions in fakemeta_util.inc
Function | Description  
---|---  
[fm_entity_range](https://amxx-bg.info/api/fakemeta_util/fm_entity_range) | ```
stock fm_get_decal_index(const decalname[])
return engfunc(EngFunc_DecalIndex, decalname)
```
  
[fm_find_ent_by_owner](https://amxx-bg.info/api/fakemeta_util/fm_find_ent_by_owner) | ```
stock fm_find_ent_by_class(index, const classname[])
return engfunc(EngFunc_FindEntityByString, index, "classname", classname)
```
  
[fm_find_ent_by_model](https://amxx-bg.info/api/fakemeta_util/fm_find_ent_by_model) | ```
stock fm_find_ent_by_tname(index, const targetname[])
return engfunc(EngFunc_FindEntityByString, index, "targetname", targetname)
```
  
[fm_entity_set_origin](https://amxx-bg.info/api/fakemeta_util/fm_entity_set_origin) | ```
stock fm_is_valid_ent(index)
return pev_valid(index)
```
  
[fm_trace_line](https://amxx-bg.info/api/fakemeta_util/fm_trace_line) | ```
stock fm_point_contents(const Float:point[3])
return engfunc(EngFunc_PointContents, point)
```
  
[fm_trace_hull](https://amxx-bg.info/api/fakemeta_util/fm_trace_hull) | ```
This function has no description.
```
  
[fm_trace_normal](https://amxx-bg.info/api/fakemeta_util/fm_trace_normal) | ```
This function has no description.
```
  
[fm_get_grenade_id](https://amxx-bg.info/api/fakemeta_util/fm_get_grenade_id) | ```
This function has no description.
```
  
[fm_playback_event](https://amxx-bg.info/api/fakemeta_util/fm_playback_event) | ```
stock fm_attach_view(index, entity)
return engfunc(EngFunc_SetView, index, entity)
```
  
[fm_is_in_viewcone](https://amxx-bg.info/api/fakemeta_util/fm_is_in_viewcone) | ```
HLSDK functions
```
  
[fm_is_visible](https://amxx-bg.info/api/fakemeta_util/fm_is_visible) | ```
This function has no description.
```
  
[fm_fakedamage](https://amxx-bg.info/api/fakemeta_util/fm_fakedamage) | ```
Engine_stocks functions
```
  
[fm_get_brush_entity_origin](https://amxx-bg.info/api/fakemeta_util/fm_get_brush_entity_origin) | ```
stock fm_get_grenade(id)
return fm_get_grenade_id(id, "", 0)
```
  
[fm_remove_entity_name](https://amxx-bg.info/api/fakemeta_util/fm_remove_entity_name) | ```
This function has no description.
```
  
[fm_ViewContents](https://amxx-bg.info/api/fakemeta_util/fm_ViewContents) | ```
This function has no description.
```
  
[fm_get_speed](https://amxx-bg.info/api/fakemeta_util/fm_get_speed) | ```
This function has no description.
```
  
[fm_set_rendering](https://amxx-bg.info/api/fakemeta_util/fm_set_rendering) | ```
This function has no description.
```
  
[fm_set_entity_flags](https://amxx-bg.info/api/fakemeta_util/fm_set_entity_flags) | ```
This function has no description.
```
  
[fm_set_entity_visibility](https://amxx-bg.info/api/fakemeta_util/fm_set_entity_visibility) | ```
This function has no description.
```
  
[fm_set_user_velocity](https://amxx-bg.info/api/fakemeta_util/fm_set_user_velocity) | ```
stock fm_get_entity_visibility(index)
return !(pev(index, pev_effects) & EF_NODRAW)
```
  
[fm_get_user_godmode](https://amxx-bg.info/api/fakemeta_util/fm_get_user_godmode) | ```
stock fm_set_client_listen(receiver, sender, listen)
return engfunc(EngFunc_SetClientListening, receiver, sender, listen)
```
  
[fm_set_user_godmode](https://amxx-bg.info/api/fakemeta_util/fm_set_user_godmode) | ```
This function has no description.
```
  
[fm_set_user_armor](https://amxx-bg.info/api/fakemeta_util/fm_set_user_armor) | ```
This function has no description.
```
  
[fm_set_user_health](https://amxx-bg.info/api/fakemeta_util/fm_set_user_health) | ```
This function has no description.
```
  
[fm_set_user_origin](https://amxx-bg.info/api/fakemeta_util/fm_set_user_origin) | ```
This function has no description.
```
  
[fm_set_user_rendering](https://amxx-bg.info/api/fakemeta_util/fm_set_user_rendering) | ```
This function has no description.
```
  
[fm_give_item](https://amxx-bg.info/api/fakemeta_util/fm_give_item) | ```
This function has no description.
```
  
[fm_set_user_maxspeed](https://amxx-bg.info/api/fakemeta_util/fm_set_user_maxspeed) | ```
This function has no description.
```
  
[fm_get_user_maxspeed](https://amxx-bg.info/api/fakemeta_util/fm_get_user_maxspeed) | ```
This function has no description.
```
  
[fm_set_user_gravity](https://amxx-bg.info/api/fakemeta_util/fm_set_user_gravity) | ```
This function has no description.
```
  
[fm_get_user_gravity](https://amxx-bg.info/api/fakemeta_util/fm_get_user_gravity) | ```
This function has no description.
```
  
[fm_spawn](https://amxx-bg.info/api/fakemeta_util/fm_spawn) | ```
This function has no description.
```
  
[fm_set_user_noclip](https://amxx-bg.info/api/fakemeta_util/fm_set_user_noclip) | ```
interferes with FM_Spawn enum, just use fm_DispatchSpawn
stock fm_spawn(entity) {
return dllfunc(DLLFunc_Spawn, entity)
}
```
  
[fm_strip_user_weapons](https://amxx-bg.info/api/fakemeta_util/fm_strip_user_weapons) | ```
stock fm_get_user_noclip(index)
return (pev(index, pev_movetype) == MOVETYPE_NOCLIP)
```
  
[fm_set_user_frags](https://amxx-bg.info/api/fakemeta_util/fm_set_user_frags) | ```
This function has no description.
```
  
[fm_cs_user_spawn](https://amxx-bg.info/api/fakemeta_util/fm_cs_user_spawn) | ```
Cstrike functions
```
  
[fm_set_kvd](https://amxx-bg.info/api/fakemeta_util/fm_set_kvd) | ```
Custom functions
```
  
[fm_find_ent_by_integer](https://amxx-bg.info/api/fakemeta_util/fm_find_ent_by_integer) | ```
This function has no description.
```
  
[fm_find_ent_by_flags](https://amxx-bg.info/api/fakemeta_util/fm_find_ent_by_flags) | ```
This function has no description.
```
  
[fm_distance_to_box](https://amxx-bg.info/api/fakemeta_util/fm_distance_to_box) | ```
This function has no description.
```
  
[fm_boxes_distance](https://amxx-bg.info/api/fakemeta_util/fm_boxes_distance) | ```
This function has no description.
```
  
[fm_distance_to_boxent](https://amxx-bg.info/api/fakemeta_util/fm_distance_to_boxent) | ```
This function has no description.
```
  
[fm_boxents_distance](https://amxx-bg.info/api/fakemeta_util/fm_boxents_distance) | ```
This function has no description.
```
  
[fm_distance_to_floor](https://amxx-bg.info/api/fakemeta_util/fm_distance_to_floor) | ```
This function has no description.
```
  
[fm_kill_entity](https://amxx-bg.info/api/fakemeta_util/fm_kill_entity) | ```
This function has no description.
```
  
[fm_get_user_weapon_entity](https://amxx-bg.info/api/fakemeta_util/fm_get_user_weapon_entity) | ```
This function has no description.
```
  
[fm_strip_user_gun](https://amxx-bg.info/api/fakemeta_util/fm_strip_user_gun) | ```
This function has no description.
```
  
[fm_transfer_user_gun](https://amxx-bg.info/api/fakemeta_util/fm_transfer_user_gun) | ```
This function has no description.
```
  
[fm_is_ent_visible](https://amxx-bg.info/api/fakemeta_util/fm_is_ent_visible) | ```
This function has no description.
```
  
[fm_get_aim_origin](https://amxx-bg.info/api/fakemeta_util/fm_get_aim_origin) | ```
This function has no description.
```
  
[fm_get_user_longjump](https://amxx-bg.info/api/fakemeta_util/fm_get_user_longjump) | ```
This function has no description.
```
  
[fm_set_user_longjump](https://amxx-bg.info/api/fakemeta_util/fm_set_user_longjump) | ```
This function has no description.
```
  
[fm_get_user_suit](https://amxx-bg.info/api/fakemeta_util/fm_get_user_suit) | ```
This function has no description.
```
  
[fm_set_user_suit](https://amxx-bg.info/api/fakemeta_util/fm_set_user_suit) | ```
This function has no description.
```
  
[fm_cs_remove_decals](https://amxx-bg.info/api/fakemeta_util/fm_cs_remove_decals) | ```
This function has no description.
```
  
[fm_is_ent_classname](https://amxx-bg.info/api/fakemeta_util/fm_is_ent_classname) | ```
This function has no description.
```
  
[fm_user_kill](https://amxx-bg.info/api/fakemeta_util/fm_user_kill) | ```
This function has no description.
```
  
[fm_get_view_angle_diff](https://amxx-bg.info/api/fakemeta_util/fm_get_view_angle_diff) | ```
This function has no description.
```
  
[fm_get_weaponbox_type](https://amxx-bg.info/api/fakemeta_util/fm_get_weaponbox_type) | ```
This function has no description.
```
  

This code is a part of fakemeta_util.inc. To use this code you should include fakemeta_util.inc as ```#include <fakemeta_util>```


  
  

