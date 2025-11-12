# set_hudmessage
#### Syntax
```
native set_hudmessage(red = 200, green = 100, blue = 0, Float:x = -1.0, Float:y = 0.35, effects = 0, Float:fxtime = 6.0, Float:holdtime = 12.0, Float:fadeintime = 0.1, Float:fadeouttime = 0.2, channel = -1);
```

#### Usage
red | ```Red component of hudmessage color```
---|---
green | ```Green component of hudmessage color```
blue | ```Blue component of hudmessage color```
x | ```Location of the message on the x axis in percent```
y | ```Location of the message on the y axis in percent```
effects | ```Display effect```
fxtime | ```Duration of the effect```
holdtime | ```Time the message stays on screen```
fadeintime | ```Time it takes the message to fully appear (fade-in)```
fadeouttime | ```Time it takes the message to fully disappear (fade-out)```
channel | ```Channel to use on the client```
#### Description
```
Sets display parameters for hudmessages.
```

#### Note
```
As of AMXX 1.61, setting the channel to -1 will automatically choose
the next available HUD channel for the client.
```

#### Note
```
There are four different HUD channels available on the client (1-4).
Sending a hudmessage to a channel will overwrite any existing messages
already displaying on that channel.
```

#### Note
```
If you plan to create a permanent message, don't forget to specify a
specific channel to avoid possible flickering due to auto-channeling.
```

#### Note
```
For the hudmessage coordinates x and y, -1.0 will center the message
on the respective axis.
```

#### Note
```
These parameters stay until the next call to set_hudmessage overwrites
them. Multiple calls to show_hudmessage will therefore re-use the same
parameters. The parameters are not stored per-plugin, so other plugins
can overwrite them.
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

