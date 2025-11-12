# xs_plane_rayintersect
#### Syntax
```
stock bool:xs_plane_rayintersect(const Float:plane[], const Float:rayStart[], const Float:rayDir[], Float:out[])
```

#### Usage
plane | ```The plane to check intersection with.```
---|---
rayStart | ```The starting point of the ray.```
rayDir | ```Direction in which the ray is going.```
out | ```The vector to copy the intersection point to, if it exists.```
#### Description
```
Checks whether a plane intersects with the ray starting at @rayStart and
going to @rayDir direction.
If it does intersect, outputs the intersection point in @out.
```

#### Return
```
true if they intersect, false otherwise.
```


This code is a part of xs.inc. To use this code you should include xs.inc as ```#include <xs>```


  
  

