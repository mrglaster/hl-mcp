elocityByAim
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
VelocityByAim - Gives you a velocity in the direction a player is looking, iVelocity is the multiplier. 
Syntax
VelocityByAim ( entity, velocity, Float:RetValue[3] ) 
Type
Native 
User Contributed Notes
tsimscabinet at msn dot com | Jun-28-04 21:51:37  
---|---  
This native can easily be manually done with more alteration. This is an example of such: new Float:vAngles[3] // plug in the view angles of the entity new Float:vReturn[3] // to get out an origin fDistance away new Float:fDistance = 400.0 // fDistance being the distance from the entity of your choice entity_get_vector(id,EV_VEC_v_angles,vAngles) vReturn[0] = floatcos( vAngles[1], degrees ) * fDistance vReturn[1] = floatsin( vAngles[1], degrees ) * fDistance vReturn[2] = floatsin( -vAngles[0], degrees ) * fDistance   
  

