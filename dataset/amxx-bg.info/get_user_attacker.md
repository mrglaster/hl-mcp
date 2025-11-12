# get_user_attacker
#### Syntax
```
native get_user_attacker(index, ...);
```

#### Usage
index | ```Client index```
---|---
... | ```If provided, the attacker weapon will be stored in an optional second parameter, and the body hit place will be stored in an optional third parameter```
#### Description
```
Returns the last known attacker of a client.
```

#### Note
```
As of AMXX 1.75 this can return a non-client entity index if the client
was attacked by a non-client entity.
```

#### Return
```
Attacker client index, a non-client entity or 0 if no
attacker was found
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

