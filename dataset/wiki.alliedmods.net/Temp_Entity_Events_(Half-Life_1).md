# Temp Entity Events (Half-Life 1)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#mw-head), [search](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#p-search)
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/index.php?title=Ru:Temp_Entity_Events_\(Half-Life_1\)&action=edit&redlink=1 "Ru:Temp Entity Events \(Half-Life 1\) \(page does not exist\)") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/Zh_cn:Temp_Entity_Events_\(Half-Life_1\) "Zh cn:Temp Entity Events \(Half-Life 1\)") |   
Add Main Description Here. 
  

## Contents
[hide] 
  * [1 Message Types](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#Message_Types)
  * [2 TempEnt Events](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#TempEnt_Events)
    * [2.1 0: TE_BEAMPOINTS](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#0:_TE_BEAMPOINTS)
    * [2.2 1: TE_BEAMENTPOINT](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#1:_TE_BEAMENTPOINT)
    * [2.3 2: TE_GUNSHOT](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#2:_TE_GUNSHOT)
    * [2.4 3: TE_EXPLOSION](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#3:_TE_EXPLOSION)
    * [2.5 4: TE_TAREXPLOSION](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#4:_TE_TAREXPLOSION)
    * [2.6 5: TE_SMOKE](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#5:_TE_SMOKE)
    * [2.7 6: TE_TRACER](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#6:_TE_TRACER)
    * [2.8 7: TE_LIGHTNING](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#7:_TE_LIGHTNING)
    * [2.9 8: TE_BEAMENTS](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#8:_TE_BEAMENTS)
    * [2.10 107: TE_EXPLODEMODEL](https://wiki.alliedmods.net/Temp_Entity_Events_\(Half-Life_1\)#107:_TE_EXPLODEMODEL)


# Message Types
Sets the type of message the temp entity is transmitted in. 
MSG_ types that can be used for _dest_ field in [message_begin](http://www.amxmodx.org/funcwiki.php?go=func&id=262) are as follows: 
```
#define MSG_BROADCAST		0	// unreliable to all
#define MSG_ONE			1	// reliable to one (msg_entity)
#define MSG_ALL			2	// reliable to all
#define MSG_INIT		3	// write to the init string
#define MSG_PVS			4	// Ents in PVS of org
#define MSG_PAS			5	// Ents in PAS of org
#define MSG_PVS_R		6	// Reliable to PVS
#define MSG_PAS_R		7	// Reliable to PAS
#define MSG_ONE_UNRELIABLE	8	// Send to one client, but don't put in reliable stream, put in unreliable datagram (could be dropped)
#define MSG_SPEC		9	// Sends to all spectator proxies
```

  

# TempEnt Events
Add Description Here. 
  

## 0: TE_BEAMPOINTS
Creates a beam between two points.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Start  | X Y Z (coords)  | Origin of primary entity, or 0 0 0  | Starting point of the beam   
End  | X Y Z (coords)  | Origin of secondary entity, or 0 0 0  | Ending point of the beam   
Sprite  | sprite path  | "sprites/laserbeam.spr"  | The sprite to use in the beam   
FrameStart  | 0-255  | 0  | The frame to start with in the sprite   
FrameRate  | 0-255  | 0  | The frame rate to show the sprite at, in 0.1s (10 = 1 fps)   
Life  | 0-255  | 50  | The length of time the beam shall remain, in 0.1s (50 = 5 seconds)   
Width  | 0-255  | 10  | The width of the beam in 0.1s   
Noise  | 0-255  | 10  | The noise amplitude of the beam, this controls how much the beam distorts, again in 0.1s   
Color  | R G B  | 255 255 255  | The color of the beam in the RBG triplet value   
Brightness  | 0-255  | 127  | The brightness of the beam   
Scroll  | 0-255  | 0  | The scroll speed of the beam, in 0.1s (??)   
  
Format
```
#define TE_BEAMPOINTS 0		// beam effect between two points


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_BEAMPOINTS)
write_coord()	// start position
write_coord()
write_coord()
write_coord()	// end position
write_coord()
write_coord()
write_short()	// sprite index
write_byte()	// starting frame
write_byte()	// frame rate in 0.1's
write_byte()	// life in 0.1's
write_byte()	// line width in 0.1's
write_byte()	// noise amplitude in 0.01's
write_byte()	// Red
write_byte()	// Green
write_byte()	// Blue
write_byte()	// brightness
write_byte()	// scroll speed in 0.1's
message_end()
```

  

## 1: TE_BEAMENTPOINT
Creates a beam between the primary entity and a point.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Start Entity  | ID of Entity  | Primary entity id  | Starting point of the beam from the id's origin   
End  | X Y Z (coords)  | Origin of secondary entity, or 0 0 0  | Ending point of the beam   
Sprite  | sprite path  | "sprites/laserbeam.spr"  | The sprite to use in the beam   
FrameStart  | 0-255  | 0  | The frame to start with in the sprite   
FrameRate  | 0-255  | 0  | The frame rate to show the sprite at, in 0.1s (10 = 1 fps)   
Life  | 0-255  | 50  | The length of time the beam shall remain, in 0.1s (50 = 5 seconds)   
Width  | 0-255  | 10  | The width of the beam in 0.1s   
Noise  | 0-255  | 10  | The noise amplitude of the beam, this controls how much the beam distorts, again in 0.1s   
Color  | R G B  | 255 255 255  | The color of the beam in the RBG triplet value   
Brightness  | 0-255  | 127  | The brightness of the beam   
Scroll  | 0-255  | 0  | The scroll speed of the beam, in 0.1s (??)   
  
Format
```
#define TE_BEAMENTPOINT 1	// beam effect between point and entity


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_BEAMENTPOINT)
write_short()	// start entity
write_coord()	// end position
write_coord()
write_coord()
write_short()	// sprite index
write_byte()	// starting frame
write_byte()	// frame rate in 0.1's
write_byte()	// life in 0.1's
write_byte()	// line width in 0.1's
write_byte()	// noise amplitude in 0.01's
write_byte()	// Red
write_byte()	// Green
write_byte()	// Blue
write_byte()	// brightness
write_byte()	// scroll speed in 0.1's
message_end()
```

  

## 2: TE_GUNSHOT
Creates a particle effect plus a ricochet sound.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Pos  | X Y Z (coords)  | Origin of primary entity, or 0 0 0  | Position of the gunshot effect   
  
Format
```
#define TE_GUNSHOT 2		// particle effect plus ricochet sound


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_GUNSHOT)
write_coord()	// start position
write_coord()
write_coord()
message_end()
```

  

## 3: TE_EXPLOSION
Creates an additive sprite, 2 dynamic lights, flickering particles, explosion sound, and moves the sprite vertically.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Pos  | X Y Z (coords)  | Origin of primary entity, or 0 0 0  | Position of the explosion effect   
Sprite  | sprite path  | "sprites/zerogxplode.spr"  | The additive sprite to use in the explosion   
Scale  | 0-255  | 1  | The scale of the sprite in the explosion, in 0.1s   
FrameRate  | 0-255  | 0  | The frame rate to show the sprite at, in 0.1s (10 = 1 fps)   
Flags  | 0-15  | 0  | Sets flags for the explosion, you may also add these together: 
  * 0: Default Half-Life explosion
  * 1: Sprite will be drawn opaque
  * 2: Do not render the dynamic lights
  * 4: Do not play the explosion sound
  * 8: Do not draw the particles

  
  
Format
```
#define TE_EXPLOSION 3		// additive sprite, 2 dynamic lights, flickering particles, explosion sound, move vertically 8 pps


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_EXPLOSION)
write_coord()	// start position
write_coord()
write_coord()
write_short()	// sprite index
write_byte()	// scale in 0.1's
write_byte()	// framerate
write_byte()	// flags
message_end()
```

  

## 4: TE_TAREXPLOSION
Creates the Quake 'tar' explosion.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Pos  | X Y Z (coords)  | Origin of primary entity, or 0 0 0  | Position of the effect   
  
Format
```
#define TE_TAREXPLOSION 4	// Quake1 "tarbaby" explosion with sound


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_TAREXPLOSION)
write_coord()	// start position
write_coord()
write_coord()
message_end()
```

  

## 5: TE_SMOKE
Creates a rising alphablend sprite at 30 pps.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Pos  | X Y Z (coords)  | Origin of primary entity, or 0 0 0  | Position of the smoke effect   
Sprite  | sprite path  | "sprites/steam1.spr"  | The alphablend sprite to use for smoke   
Scale  | 0-255  | 1  | The scale of the smoke, in 0.1s   
FrameRate  | 0-255  | 0  | The frame rate to show the sprite at   
  
Format
```
#define TE_SMOKE 5			// alphablend sprite, move vertically 30 pps


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_SMOKE)
write_coord()	// start position
write_coord()
write_coord()
write_short()	// sprite index 
write_byte()	// scale in 0.1's 
write_byte()	// framerate 
message_end()
```

  

## 6: TE_TRACER
Creates a tracer effect from one point to another.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Pos  | X Y Z (coords)  | Origin of primary entity, or 0 0 0  | Starting point of the tracer   
End  | X Y Z (coords)  | Origin of secondary entity, or 0 0 0  | Ending point of the tracer   
  
Format
```
#define TE_TRACER 6			// tracer effect from point to point


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_TRACER)
write_coord()	// start position
write_coord()
write_coord()
write_coord()	// end position 
write_coord()
write_coord()
message_end()
```

  

## 7: TE_LIGHTNING
Simplified options for TE_BEAMPOINTS - Lightning effect.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Pos  | X Y Z (coords)  | Origin of primary entity, or 0 0 0  | Starting point of the lightning   
End  | X Y Z (coords)  | Origin of secondary entity, or 0 0 0  | Ending point of the lightning   
Life  | 0-255  | 50  | The length of time the lightning shall remain, in 0.1s (50 = 5 seconds)   
Width  | 0-255  | 10  | The width of the lightning in 0.1s   
Noise  | 0-255  | 10  | The noise amplitude of the lightning, this controls how much it distorts, again in 0.1s   
Sprite  | sprite path  | "sprites/laserbeam.spr"  | The sprite to use in the lightning   
  
Format
```
#define TE_LIGHTNING 7		// TE_BEAMPOINTS with simplified parameters


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_LIGHTNING)
write_coord()	// start position
write_coord()
write_coord()
write_coord()	// end position 
write_coord()
write_coord()
write_byte()	// life in 0.1's 
write_byte()	// width in 0.1's 
write_byte()	// amplitude in 0.01's 
write_short()	// sprite model index
message_end()
```

  

## 8: TE_BEAMENTS
Creates a beam between the primary entity and another entity.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Start Entity  | ID of Entity  | Primary entity id  | Starting point of the beam from the id's origin   
End Entity  | ID of Entity  | Secondary entity id  | Ending point of the beam to the id's origin   
Sprite  | sprite path  | "sprites/laserbeam.spr"  | The sprite to use in the beam   
FrameStart  | 0-255  | 0  | The frame to start with in the sprite   
FrameRate  | 0-255  | 0  | The frame rate to show the sprite at, in 0.1s (10 = 1 fps)   
Life  | 0-255  | 50  | The length of time the beam shall remain, in 0.1s (50 = 5 seconds)   
Width  | 0-255  | 10  | The width of the beam in 0.1s   
Noise  | 0-255  | 10  | The noise amplitude of the beam, this controls how much the beam distorts, again in 0.1s   
Color  | R G B  | 255 255 255  | The color of the beam in the RBG triplet value   
Brightness  | 0-255  | 127  | The brightness of the beam   
Scroll  | 0-255  | 0  | The scroll speed of the beam, in 0.1s (??)   
  
Format
```
#define TE_BEAMENTS 8		// Create a beam between two entities


message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_BEAMENTS)
write_short()	// start entity
write_short()  // end entity
write_short()	// sprite index
write_byte()	// starting frame
write_byte()	// frame rate in 0.1's
write_byte()	// life in 0.1's
write_byte()	// line width in 0.1's
write_byte()	// noise amplitude in 0.01's
write_byte()	// red
write_byte()	// green
write_byte()	// blue
write_byte()	// brightness
write_byte()	// scroll speed in 0.1's
message_end()
```

## 107: TE_EXPLODEMODEL
Spherical shower of models, picks from set.
  
Options
Option | Range | Default | Description   
---|---|---|---  
Pos  | X Y Z (coords)  | Origin of primary entity, or 0 0 0  | Position of the explode model effect   
Velocity  | 1-255  | 10  | The velocity of explode model.   
Model Index  | model path  | "models/gib_skull.mdl"  | The file path of model to explode.   
Count  | 1-1000  | 1  | The number of models used.   
Life  | 0-255  | 50  | The length of time the models with remain and blink, in 0.1s (50 = 5 seconds)   
Format
```
#define TE_EXPLODEMODEL             107

message_begin(MSG_ ,SVC_TEMPENTITY)
write_byte(TE_EXPLODEMODEL)
write_coord(origin.x)
write_coord(origin.y)
write_coord(origin.z)
write_coord(velocity)
write_short(model index)
write_short(count)
write_byte(life in 0.1's)
message_end()

```

TODO: add rest, I'll get this done eventually. 
