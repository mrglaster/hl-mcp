# get_user_authid
#### Syntax
```
native get_user_authid(index, authid[], len);
```

#### Usage
index | ```Client index```
---|---
authid | ```Buffer to copy auth to```
len | ```Maximum buffer size```
#### Description
```
Retrieves the SteamID of a client.
```

#### Note
```
The SteamID is only available once the client_authorized() forward has
been called for the client.
```

#### Return
```
Number of cells written to buffer
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

