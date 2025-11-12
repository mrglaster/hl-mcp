# next_hudchannel
#### Syntax
```
native next_hudchannel(player);
```

#### Usage
player | ```Client index```
---|---
#### Description
```
Returns the next valid hudchannel for the client.
```

#### Note
```
This function uses the same method set_hudmessage() uses to determine
the next channel if it is set to auto-select.
```

#### Return
```
Valid hudchannel (1-4)
```

#### Error
```
If the index is not within the range of 1 to MaxClients or
the client is not connected, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

