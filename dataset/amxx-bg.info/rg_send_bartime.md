# rg_send_bartime
#### Syntax
```
native rg_send_bartime(const index, const duration, const bool:observer = true);
```

#### Usage
index | ```Client index```
---|---
time | ```Duration```
observer | ```Send for everyone who is observing the player```
#### Description
```
Draws a HUD progress bar which fills from 0% to 100% for the time duration in seconds.
```

#### Note
```
: Set the duration to 0 to hide the bar.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.