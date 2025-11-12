# register_touch
#### Syntax
```
native register_touch(const Touched[], const Toucher[], const function[]);
```

#### Usage
Touched | ```Entity classname being touched, "*" or "" for any class```
---|---
Toucher | ```Entity classname touching, "*" or "" for any class```
function | ```Name of callback function```
#### Description
```
Registers a function to be called on a touch action between entities of
specified classes.
```

#### Note
```
The function will be called in the following manner:

public touch_handler(touched, toucher)

  touched    - Index of entity being touched
  toucher    - Index of entity touching
```

#### Note
```
The callback should return PLUGIN_CONTINUE to ignore the touch,
PLUGIN_HANDLED or higher to block it.
```

#### Note
```
When returning PLUGIN_HANDLED from the callback, Engine will still fire
other touch functions like the pfn_touch() forward before actually
blocking the touch. To immediately block return PLUGIN_HANDLED_MAIN
instead.
```

#### Return
```
Touch forward id
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

