# set_native_filter
#### Syntax
```
native set_native_filter(const handler[]);
```

#### Usage
handler | ```Function name to call```
---|---
#### Description
```
Sets a native filter, letting the plugin intercept and handle an
automatic native requirement.
```

#### Note
```
This has to be used inside the plugin_native() forward, otherwise it
has no effect.
```

#### Note
```
This is useful for creating plugins that can dynamically decide which
modules or features to use at runtime, often necessary for cross-mod
plugins. It allows to deploy a single version of the plugin instead
of compiling multiple versions for each use-case.
```

#### Note
```
The handler will be called in the following manner:

public native_filter(const native[], index, trap)

  native      - Native name
  index       - Native index
  trap        - 0 if native couldn't be found, 1 if native use was attempted
```

#### Note
```
The handler should return PLUGIN_CONTINUE to let the error through the
filter (which will throw a run-time error), or return PLUGIN_HANDLED
to continue operation.
```

#### Note
```
Returning PLUGIN_CONTINUE if trap is 0 will result in the plugin
failing to load!
```

#### Return
```
1 if handler is set successfully, 0 otherwise (called
outside of plugin_native() forward)
```

#### Error
```
If an invalid callback function is provided, an error is
thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

