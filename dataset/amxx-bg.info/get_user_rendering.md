# get_user_rendering
#### Syntax
```
native get_user_rendering(index, &fx = kRenderFxNone, &r = 0, &g = 0, &b = 0, &render = kRenderNormal, &amount = 0);
```

#### Usage
index | ```Client index```
---|---
fx | ```Variable to store the rendering effect```
r | ```Variable to store the amount of red color```
g | ```Variable to store the amount of green color```
b | ```Variable to store the amount of blue color```
render | ```Variable to store the render mode```
amount | ```Variable to store the render amount```
#### Description
```
Gets player's rendering mode.
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


  
  

