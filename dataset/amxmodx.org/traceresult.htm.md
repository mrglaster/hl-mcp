raceresult
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
traceresult - Returns information from the last traceresult. 
Syntax
traceresult ( type, [ ... ] ) 
Type
Native 
Notes
```
  
TR_AllSolid,		// (int) if true, plane is not valid
  
TR_StartSolid,		// (int) if true, the initial point was in a solid area
  
TR_InOpen,		// (int)
  
TR_InWater,		// (int)
  
TR_Fraction,		// (float) time completed, 1.0 = didn't hit anything
  
TR_EndPos,		// (vector) final position
  
TR_PlaneDist,		// (float)
  
TR_PlaneNormal,		// (vector) surface normal at impact
  
TR_Hit,			// (entity) entity the surface is on
  
TR_Hitgroup		// (int) 0 == generic, non zero is specific body part
  

```

