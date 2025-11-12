# set_client_listen
#### Syntax
```
native set_client_listen(receiver, sender, listen);
```

#### Usage
receiver | ```Receiver```
---|---
sender | ```Sender```
listen | ```1 if receiver should be able to hear sender, 0 if not```
#### Description
```
Sets who can listen who.
```

#### Return
```
0 if the setting can't be done for some reason
```

#### Error
```
If receiver or sender are not connected or not
within the range of 1 to MaxClients.
```


This code is a part of fun.inc. To use this code you should include fun.inc as ```#include <fun>```


  
  

