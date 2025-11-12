# Functions in msgstocks.inc
Function | Description  
---|---  
[draw_ammo_pickup_icon](https://amxx-bg.info/api/msgstocks/draw_ammo_pickup_icon) | ```
Temporarily draws HUD numerical ammo amount and corresponding ammo
HUD icon in the middle of the right side of the screen.
```
  
[draw_item_pickup_icon](https://amxx-bg.info/api/msgstocks/draw_item_pickup_icon) | ```
Temporarily draws a corresponding item HUD icon in the middle of the
right side of the screen.
```
  
[draw_weapon_pickup_icon](https://amxx-bg.info/api/msgstocks/draw_weapon_pickup_icon) | ```
Temporarily draws the corresponding weapon HUD icon in the middle of the
right side of the screen.
```
  
[draw_status_icon](https://amxx-bg.info/api/msgstocks/draw_status_icon) | ```
Draws a specified status HUD icon.
```
  
[draw_train_controls](https://amxx-bg.info/api/msgstocks/draw_train_controls) | ```
Displays the speed bar used for controlling a train.
```
  
[send_geiger_signal](https://amxx-bg.info/api/msgstocks/send_geiger_signal) | ```
Sends the geiger signal that notifies the player of nearby radiation level.
```
  
[hide_hud_elements](https://amxx-bg.info/api/msgstocks/hide_hud_elements) | ```
Hides specific elements from the HUD.
```
  
[fade_user_screen](https://amxx-bg.info/api/msgstocks/fade_user_screen) | ```
Fades the client's screen.
```
  
[shake_user_screen](https://amxx-bg.info/api/msgstocks/shake_user_screen) | ```
Shakes the client's screen.
```
  
[set_user_fov](https://amxx-bg.info/api/msgstocks/set_user_fov) | ```
Changes the client's field of view (FOV).
```
  
[cs_draw_progress_bar](https://amxx-bg.info/api/msgstocks/cs_draw_progress_bar) | ```
Draws a HUD progress bar which is filled from 0% to 100% for the given
amount of seconds. Once the bar is fully filled it will be removed from
the screen automatically.
```
  
[cs_play_reload_sound](https://amxx-bg.info/api/msgstocks/cs_play_reload_sound) | ```
Plays a generic reload sound.
```
  
[cs_set_hud_icon](https://amxx-bg.info/api/msgstocks/cs_set_hud_icon) | ```
Displays a sprite to the right side of the round timer.
```
  
[cs_set_user_shadow](https://amxx-bg.info/api/msgstocks/cs_set_user_shadow) | ```
Creates/Hides the shadow beneath players.
```
  
[te_create_beam_between_points](https://amxx-bg.info/api/msgstocks/te_create_beam_between_points) | ```
Creates a beam between two points.
```
  
[te_create_beam_from_entity](https://amxx-bg.info/api/msgstocks/te_create_beam_from_entity) | ```
Creates a beam between an entity and a point.
```
  
[te_create_gunshot](https://amxx-bg.info/api/msgstocks/te_create_gunshot) | ```
Creates a gunshot that consists of a particle effect and a ricochet sound.
```
  
[te_create_explosion](https://amxx-bg.info/api/msgstocks/te_create_explosion) | ```
Creates an explosion.
```
  
[te_create_tar_explosion](https://amxx-bg.info/api/msgstocks/te_create_tar_explosion) | ```
Creates the Quake "tarbaby" explosion with sound.
```
  
[te_create_smoke](https://amxx-bg.info/api/msgstocks/te_create_smoke) | ```
Creates smoke (a rising alphablend sprite at 30 pps).
```
  
[te_create_tracer](https://amxx-bg.info/api/msgstocks/te_create_tracer) | ```
Creates a tracer effect from one point to another.
```
  
[te_create_beam_between_entities](https://amxx-bg.info/api/msgstocks/te_create_beam_between_entities) | ```
Creates a beam between two entities.
```
  
[te_create_sparks](https://amxx-bg.info/api/msgstocks/te_create_sparks) | ```
Creates 8 random tracers with gravity and a ricochet sprite.
```
  
[te_create_lava_splash](https://amxx-bg.info/api/msgstocks/te_create_lava_splash) | ```
Creates a Quake-style lava splash.
```
  
[te_create_teleport_splash](https://amxx-bg.info/api/msgstocks/te_create_teleport_splash) | ```
Creates a Quake-style teleport splash.
```
  
[te_create_colored_explosion](https://amxx-bg.info/api/msgstocks/te_create_colored_explosion) | ```
Creates a Quake colormapped (base palette) particle explosion with sound.
```
  
[te_place_decal_from_bsp_file](https://amxx-bg.info/api/msgstocks/te_place_decal_from_bsp_file) | ```
Places a decal from the .BSP file.
```
  
[te_create_implosion](https://amxx-bg.info/api/msgstocks/te_create_implosion) | ```
Creates tracers moving towards a point.
```
  
[te_create_model_trail](https://amxx-bg.info/api/msgstocks/te_create_model_trail) | ```
Creates a line of moving glow sprites or models with gravity, fadeout,
and collisions.
```
  
[te_display_additive_sprite](https://amxx-bg.info/api/msgstocks/te_display_additive_sprite) | ```
Displays an additive sprite that plays one cycle.
```
  
[te_create_beam_sprite](https://amxx-bg.info/api/msgstocks/te_create_beam_sprite) | ```
Creates a beam with a sprite at the end of the beam.
```
  
[te_create_beam_ring](https://amxx-bg.info/api/msgstocks/te_create_beam_ring) | ```
Creates a screen aligned beam ring that expands to the maximum radius
over lifetime.
```
  
[te_create_beam_disk](https://amxx-bg.info/api/msgstocks/te_create_beam_disk) | ```
Creates a beam disk that expands to the maximum radius over lifetime.
```
  
[te_create_beam_cylinder](https://amxx-bg.info/api/msgstocks/te_create_beam_cylinder) | ```
Creates a beam cylinder that expands to the maximum radius over lifetime.
```
  
[te_create_following_beam](https://amxx-bg.info/api/msgstocks/te_create_following_beam) | ```
Creates a decaying beam that follows the entity until it stops moving.
```
  
[te_display_glow_sprite](https://amxx-bg.info/api/msgstocks/te_display_glow_sprite) | ```
Displays a glowing sprite.
```
  
[te_create_beam_ring_between_ent](https://amxx-bg.info/api/msgstocks/te_create_beam_ring_between_ent) | ```
Creates a beam ring between two entities.
```
  
[te_create_tracer_shower](https://amxx-bg.info/api/msgstocks/te_create_tracer_shower) | ```
Creates an oriented shower of tracers.
```
  
[te_create_dynamic_light](https://amxx-bg.info/api/msgstocks/te_create_dynamic_light) | ```
Creates a dynamic light with a world effect.
```
  
[te_create_entity_light](https://amxx-bg.info/api/msgstocks/te_create_entity_light) | ```
Creates a point entity light with no world effect.
```
  
[te_draw_line](https://amxx-bg.info/api/msgstocks/te_draw_line) | ```
Draws a simple line.
```
  
[te_create_box](https://amxx-bg.info/api/msgstocks/te_create_box) | ```
Creates a simple box.
```
  
[te_remove_all_beams_from_entity](https://amxx-bg.info/api/msgstocks/te_remove_all_beams_from_entity) | ```
Removes all beams attached to an entity.
```
  
[te_create_large_funnel](https://amxx-bg.info/api/msgstocks/te_create_large_funnel) | ```
Creates a large group of sprites or models accompanied by green dots
that float up or down until they reach the point set in the "position" argument.
```
  
[te_create_bloodstream](https://amxx-bg.info/api/msgstocks/te_create_bloodstream) | ```
Creates dripping blood particles.
```
  
[te_draw_blood_line](https://amxx-bg.info/api/msgstocks/te_draw_blood_line) | ```
Draws a line of blood particles spread 5 units from each other that
disappears after 30 seconds.
```
  
[te_spray_blood](https://amxx-bg.info/api/msgstocks/te_spray_blood) | ```
Sprays blood particles from a given point.
```
  
[te_place_brush_decal](https://amxx-bg.info/api/msgstocks/te_place_brush_decal) | ```
Applies a decal to a brush entity (not the world).
```
  
[te_create_bouncing_model](https://amxx-bg.info/api/msgstocks/te_create_bouncing_model) | ```
Creates a moving model or sprite that bounces and makes a sound when it hits.
```
  
[te_create_explode_model](https://amxx-bg.info/api/msgstocks/te_create_explode_model) | ```
Creates model or sprite with a blinking orange aura effect.
```
  
[te_create_break_model](https://amxx-bg.info/api/msgstocks/te_create_break_model) | ```
Creates a model or sprite entity that slowly disappears until it's gone.
```
  
[te_place_gunshot_decal](https://amxx-bg.info/api/msgstocks/te_place_gunshot_decal) | ```
Places a gunshot decal on an entity or the world and plays a ricochet sound.
```
  
[te_create_sprite_spray](https://amxx-bg.info/api/msgstocks/te_create_sprite_spray) | ```
Creates a spray of alpha sprites or models.
```
  
[te_create_armor_ricochet](https://amxx-bg.info/api/msgstocks/te_create_armor_ricochet) | ```
Creates a quick spray sprite with a ricochet sound.
```
  
[te_place_player_spray](https://amxx-bg.info/api/msgstocks/te_place_player_spray) | ```
Places a player spray on an entity or the world.
```
  
[te_create_bubble_box](https://amxx-bg.info/api/msgstocks/te_create_bubble_box) | ```
Creates alpha sprites or models inside of a box that float upwards.
```
  
[te_create_bubble_line](https://amxx-bg.info/api/msgstocks/te_create_bubble_line) | ```
Creates alpha sprites or models along a line that float upwards.
```
  
[te_display_falling_sprite](https://amxx-bg.info/api/msgstocks/te_display_falling_sprite) | ```
Creates an spray of opaque sprites or models that fall to another sprite or model.
```
  
[te_place_world_decal](https://amxx-bg.info/api/msgstocks/te_place_world_decal) | ```
Applies a decal to the world brush.
```
  
[te_create_projectile](https://amxx-bg.info/api/msgstocks/te_create_projectile) | ```
Creates a nail-like projectile.
```
  
[te_create_sprite_shower](https://amxx-bg.info/api/msgstocks/te_create_sprite_shower) | ```
Creates a shower of sprites or models.
```
  
[te_emit_sprite_from_player](https://amxx-bg.info/api/msgstocks/te_emit_sprite_from_player) | ```
Emits sprites or models from a player's bounding box.
```
  
[te_create_particle_burst](https://amxx-bg.info/api/msgstocks/te_create_particle_burst) | ```
Creates a particle burst similar to te_create_lava_splash.
```
  
[te_create_fire_field](https://amxx-bg.info/api/msgstocks/te_create_fire_field) | ```
Creates a field of fire.
```
  
[te_attach_model_to_player](https://amxx-bg.info/api/msgstocks/te_attach_model_to_player) | ```
Attaches a temporary entity model to a client.
```
  
[te_remove_player_attachments](https://amxx-bg.info/api/msgstocks/te_remove_player_attachments) | ```
Kills all temporary entity models attached to a client.
```
  
[te_create_multi_gunshot](https://amxx-bg.info/api/msgstocks/te_create_multi_gunshot) | ```
Much more compact shotgun shot stock.
```
  
[te_create_user_tracer](https://amxx-bg.info/api/msgstocks/te_create_user_tracer) | ```
Creates a tracer effect and allows more customization than te_create_tracer.
```
  
[get_msg_destination](https://amxx-bg.info/api/msgstocks/get_msg_destination) | ```
Used with message stocks. Returns whether or not to use the reliable or
unreliable channel when sending a message according to the params used.
```
  
[float_to_short](https://amxx-bg.info/api/msgstocks/float_to_short) | ```
Converts a float value into a short.
```
  

This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.