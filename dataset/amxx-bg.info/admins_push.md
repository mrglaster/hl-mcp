# admins_push
#### Syntax
```
native admins_push(const AuthData[], const Password[], Access, Flags);
```

#### Usage
AuthData | ```Auth information to set (can be name, IP or SteamID)```
---|---
Password | ```Password to set```
Access | ```Admin access flags```
Flags | ```Auth behavior flags```
#### Description
```
Adds an admin to the dynamic admin storage for lookup at a later time.
```

#### Note
```
For a list of possible access flags, see the ADMIN_* constants in
amxconst.inc
```

#### Note
```
For a list of possible auth flags, see the FLAG_* constants in
amxconst.inc
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

