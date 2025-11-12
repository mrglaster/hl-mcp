# register_impulse
#### Syntax
```
native register_impulse(impulse, const function[]);
```

#### Usage
impulse | ```Impulse to hook```
---|---
function | ```Name of callback function```
#### Description
```
Registers a function to be called on a client impulse.
```

#### Note
```
The function will be called in the following manner:

public impulse_handler(client, impulse)

  client     - Client index
  impulse    - Impulse triggered by the client
```

#### Note
```
The callback should return PLUGIN_CONTINUE to ignore the impulse,
PLUGIN_HANDLED or higher to nullify it (CmdStart() is not blocked).
```

#### Note
```
When returning PLUGIN_HANDLED or higher from the callback, Engine will
still fire other impulse functions. This includes the client_impulse()
and client_cmdStart() forwards.
```

#### Return
```
Impulse forward id
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

