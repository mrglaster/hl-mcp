# Vectors Explained (Scripting)

Vectors in general tend to be rather confusing until they are explained. There are three different types you will see. Position Vectors, Velocity Vectors, and Angle Vectors. While in most basic cases you will probably only use one of these at a time, it doesn't hurt to know what the other two parameters are there for. Here is an example of the native 'TeleportEntity' to show you what it looks like: 

```
native int TeleportEntity(int entity, const float origin[3], const float angles[3], const float velocity[3]);
```

## Positions
**Position Vector** : The first Vector in this native, declared as origin[3], is the Position Vector. This simply tells us the entities absolute position in the world. The position vector could look something like {15.0, 30.0, 15.0} and this would mean the entity is 15 units along the X axis, 30 units along the Y axis, and 15 units along the Z axis. 

## Angles
**Angles** specify the _angles_ of the rotation, not the actual vector of the rotation! (Essentially, it's an arctangent of each direction component.) Angles are specified as `{pitch/up, yaw/left, roll/spin}}`. Angles are specified as a `float[3]` array. Angles can be turned into a vector (and back into an angle!) using the angle natives: `GetAngleVectors` and `GetVectorAngles`. 
Most angles are sanitized between -180 and 180 within the source engine (for up/down on players this is -89/89!), however some weird physics shenanigans and cheating clients can exceed these values so always ensure your angles are well formed before using them. 
![](https://wiki.alliedmods.net/images/thumb/Silly_goose.png/32px-Silly_goose.png)
Make sure to use `GetAngleVectors` before using the angles value to transform world space! 
##  Velocity
**Velocity** , or a **Vector** , is a true vector in the sense that it is _only a direction and magnitude_. The velocity represents motion, usually the amount of motion that will occur in one tick. The position of an object on the next tick will be the sum of the current position and the object's velocity. 
## Velocity Vectors
```
float vecOrigin[3], vecVelocity[3], vecResult[3];
 
AddVectors(vecOrigin, vecVelocity, vecResult);
```

