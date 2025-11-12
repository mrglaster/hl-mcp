# elog_message
#### Syntax
```
native elog_message(const message[], any:...);
```

#### Usage
string | ```Formatting rules```
---|---
... | ```Variable number of formatting parameters```
#### Description
```
Logs a message hookable by plugins to the current server log file.
```

#### Note
```
The log will include a timestamp with the message.
```

#### Note
```
The message can be hooked using "register_logevent".
```

#### Return
```
Number of printed characters
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

