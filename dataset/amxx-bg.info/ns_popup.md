# ns_popup
#### Syntax
```
native ns_popup(target, const szMsg[180], ah=0);
```

#### Usage
target | ```The client to receive the message.  Set to 0 to send to everybody.```
---|---
szMsg | ```The message to send, 180 characters max.```
ah | ```Whether to only display the message on clients who have the cvar "cl_autohelp" set to 1.```
#### Description
```
Send an NS-style popup message.
```

#### Return
```
This function has no return value.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).