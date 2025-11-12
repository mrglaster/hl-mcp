# set_ent_rendering
#### Syntax
```
native set_ent_rendering(index, fx = kRenderFxNone, r = 0, g = 0, b = 0, render = kRenderNormal, amount = 0);
```

#### Usage
index | ```Entity index```
---|---
fx | ```Rendering effect```
r | ```Red component of rendering color```
g | ```Green component of rendering color```
b | ```Blue component of rendering color```
render | ```Rendering mode```
amount | ```Rendering amount```
#### Description
```
Sets rendering options of an entity.
```

#### Note
```
For a list of valid rendering effects see the kRenderFx* constants in
amxconst.inc
```

#### Note
```
For a list of valid rendering modes see the kRender* constants in
amxconst.inc
```

#### Note
```
Rendering amount has different meanings depending on the rendering
effect and mode used on the entity.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

