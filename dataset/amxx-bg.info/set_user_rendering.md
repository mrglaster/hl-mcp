# set_user_rendering
#### Syntax
```
native set_user_rendering(index, fx = kRenderFxNone, r = 0, g = 0, b = 0, render = kRenderNormal, amount = 0);
```

#### Usage
index | ```Client index```
---|---
fx | ```Rendering effects. One of kRenderFx* constants```
r | ```The amount of red color (0 to 255)```
g | ```The amount of green color (0 to 255)```
b | ```The amount of blue color (0 to 255)```
render | ```Render mode. One of kRender* constants```
amount | ```Render amount (0 to 255)```
#### Description
```
Sets player's rendering mode.
```

#### Note
```
A really useful render modes reference:
https://sites.google.com/site/svenmanor/rendermodes
```

#### Return
```
This function has no return value.
```

#### Error
```
If player is not connected or not within the range
of 1 to MaxClients.
```


This code is a part of fun.inc. To use this code you should include fun.inc as ```#include <fun>```


  
  

