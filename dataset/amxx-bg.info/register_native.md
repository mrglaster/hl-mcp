# register_native
#### Syntax
```
native register_native(const name[], const handler[], style = 0);
```

#### Usage
name | ```Native name```
---|---
handler | ```Callback function```
style | ```Native style```
#### Description
```
Registers a native.
```

#### Note
```
Style 0 natives call the handler in the following manner:

public native_handler(plugin_id, argc)

  plugin_id    - plugin calling the native
  argc         - number of parameters
```

#### Note
```
Style 1 natives are deprecated. Plugins should not use them, they might
break.
```

#### Note
```
Style 1 natives work a little different. Instead of passing plugin id
and number of parameters, the handler should be prototyped just like the
native would be called. For each by-reference parameter, the plugin
then has to use param_convert() to properly use them.
```

#### Note
```
A native should *never* recurse. Bad things will happen.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid callback is specified, an error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

