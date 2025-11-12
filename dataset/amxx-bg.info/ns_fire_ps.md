# ns_fire_ps
#### Syntax
```
native ns_fire_ps(Particle:system,const Float:origin[3],const Float:angles[3]={0.0,0.0,0.0}, flags=0);
```

#### Description
```
Draws a particle system at the given origin (and angles)
Flags are the FEV_* defines from hlsdk_const.inc
Only use handles returned by ns_spawn_ps or ns_get_ps_id here!
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).