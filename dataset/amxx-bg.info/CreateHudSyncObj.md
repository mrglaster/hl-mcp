# CreateHudSyncObj
#### Syntax
```
native CreateHudSyncObj(num = 0, ...);
```

#### Usage
num | ```Unused and ignored```
---|---
... | ```Unused and ignored```
#### Description
```
Creates a HUD synchronization object.
```

#### Note
```
Create one of these for each section of the screen that contains
overlapping HUD messages. For example, if using both sides of the
screen to display three messages that could potentially overlap,
each side is considered a synchronizable area. You can then use
ShowSyncHudMsg() to correctly synchronize displaying the HUD message
with any other messages potentially in its class.
```

#### Note
```
This does not do anything like reserving screen area. Its sole
purpose is to be able to wipe an old message on an auto-channel and
ensure that it will not clear a message from another plugin.
```

#### Return
```
HUD sync object handle
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

