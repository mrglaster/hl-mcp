# client_authorized
#### Syntax
```
forward client_authorized(id, const authid[]);
```

#### Usage
id | ```Client index```
---|---
authid | ```Client auth```
#### Description
```
Called when the client gets a valid SteamID.
```

#### Note
```
This may occur before or after client_putinserver has been called.
```

#### Note
```
This is called for bots, and the SteamID will be "BOT".
```

#### Return
```
This forward ignores the return value.
```


This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

