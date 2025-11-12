# gag_user
#### Syntax
```
native gag_user(name[], ip[], duration, reason[], admin[])
```

#### Usage
name | ```Player name```
---|---
ip | ```Player IP address```
duration | ```Gag duration in minutes```
reason | ```Reason for the gag```
admin | ```Admin name who made the gag```
#### Description
```
Gags player by given name and ip
```

#### Return
```
This function has no return value.
```

#### Error
```
If the IP address is not in the valid format or
duration is negative, an error will be thrown
```


This code is a part of gagsystem.inc. To use this code you should include gagsystem.inc as ```#include <gagsystem>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.