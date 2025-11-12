# cs_draw_progress_bar
#### Syntax
```
stock cs_draw_progress_bar(id, duration, startpercent = 0, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
duration | ```How long (in seconds) until the bar is fully filled```
startpercent | ```Bar starting percentage (0-100)```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Draws a HUD progress bar which is filled from 0% to 100% for the given
amount of seconds. Once the bar is fully filled it will be removed from
the screen automatically.
```

#### Note
```
If the "startpercent" argument is greater than 0, the bar will be
filled from that amount of percentage instead of starting from 0%.
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.