# rg_send_bartime2
#### Syntax
```
native rg_send_bartime2(const index, const duration, const Float:startPercent, const bool:observer = true);
```

#### Usage
index | ```Client index```
---|---
time | ```Duration```
startPercent | ```Start percent```
observer | ```Send for everyone who is observing the player```
#### Description
```
Same as BarTime, but StartPercent specifies how much of the bar is (already) filled.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.