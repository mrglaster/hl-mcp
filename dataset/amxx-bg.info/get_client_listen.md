# get_client_listen
#### Syntax
```
native get_client_listen(receiver, sender);
```

#### Usage
receiver | ```Receiver```
---|---
sender | ```Sender```
#### Description
```
Tells whether receiver hears sender via voice communication.
```

#### Return
```
1 if receiver hears the sender, 0 otherwise.
```

#### Error
```
If receiver or sender are not connected or not
within the range of 1 to MaxClients
```


This code is a part of fun.inc. To use this code you should include fun.inc as ```#include <fun>```


  
  

